from psox import psoxglobals as G

G.SEEINTERNAL = False

PSOX_MAJOR_VER = 1
PSOX_MINOR_VER_RANGE = (0, 0)

G.PSOX_MAJOR_VER = PSOX_MAJOR_VER
G.PSOX_MINOR_VER_RANGE = PSOX_MINOR_VER_RANGE

assert PSOX_MINOR_VER_RANGE[0] <= PSOX_MINOR_VER_RANGE[1]

from optparse import OptionParser
from ConfigParser import ConfigParser
from subprocess import Popen, PIPE
import sys
from psox.errors import IllegalPSOXError, UnsupportedVersionError
from psox.utils import getlinesuntil, linelen, vn2vs, linelen_atleast
from os.path import normcase

import psox.fd

import re
REGEX1 = re.compile(r"((?:[^\x00]|\x00{2}(?:.|\Z))*)(\x00.*)?\Z", re.S)
REGEX2 = re.compile(r"\x00\x00(.)", re.S)

parser = OptionParser(usage="%prog [-s safety1,safety2] [-c \"fakecommandline\"] command", version="PSOX " + vn2vs(PSOX_MAJOR_VER, PSOX_MINOR_VER_RANGE) + " - %prog 0.0")
parser.add_option("-s", "--safety", dest="safety", help="Specifies safety options. e.g to allow full access to the filesystem, and no Internet access, use \"-s fullfileio,nonet\"")
parser.add_option("-c", "--command-line", dest="cline", help="Specifies the virtual command line for the client")

options, args = parser.parse_args()

if(options.safety is not None):
    G.SAFETYLIST = options.safety.split(",")
else:
    G.SAFETYLIST = []
    
G.CLINE = options.cline

client = Popen(args, stdin=PIPE, stdout=PIPE)

def getline():
    try:
        return client.stdout.readline()
    except IOError:
        sys.exit(0)

def send(msg):
    try:
        client.stdin.write(msg)
        client.stdin.flush()
        if(G.SEEINTERNAL): print "Sent: " + repr(msg)
    except IOError:
        sys.exit(0)
        
        
domaincfg = ConfigParser()
domaincfg.readfp(open(normcase("psox/domains.txt")))
G.DOMDICT = {}
for (i, j) in domaincfg.items("Builtin"):
    the_domain = __import__("psox."+j)
    the_domain = getattr(the_domain, j) #Because the __import__ returns the psox module
    if(the_domain.MY_VERSION): #Filter out domains with myver 0
        G.DOMDICT[int(i)] = (the_domain.MY_VERSION, the_domain.the_domain())
        



curline = getlinesuntil("", getline, linelen, 4)
if(curline[0:2]!="\x00\x07"):
    raise IllegalPSOXError
elif(curline[2] != chr(PSOX_MAJOR_VER)):
    raise UnsupportedVersionError

send("\x00")
curline = getlinesuntil("", getline, linelen, 3)

cli_min_ver, cli_max_ver = ord(curline[0]), ord(curline[1])
print "Client's PSOX Ver: PSOX " + vn2vs(PSOX_MAJOR_VER, cli_min_ver, cli_max_ver)
if(cli_min_ver > cli_max_ver):
    raise IllegalPSOXError("Client's minimum version higher than its maximum?")
if(cli_max_ver < PSOX_MINOR_VER_RANGE[0]):
    raise UnsupportedVersionError("PSOX " + vn2vs(PSOX_MAJOR_VER, cli_max_ver) + " obsolete.")
if(cli_min_ver > PSOX_MINOR_VER_RANGE[1]):
    raise UnsupportedVersionError("PSOX " + vn2vs(PSOX_MAJOR_VER, cli_min_ver) + " not supported yet.")

cliver = min(cli_max_ver, PSOX_MINOR_VER_RANGE[1])
G.CLIVER = cliver

print "Running PSOX " + vn2vs(PSOX_MAJOR_VER, cliver)


send("\x00" + chr(cliver))

FDDICT = G.FDDICT

while True:
    the_line = getline()
    #print "Well, at least I got _a_ line"
    part1, part2 = REGEX1.findall(the_line)[0]
    #print repr(part1)
    going_out = REGEX2.sub(r"\1", part1)
    FDDICT[0].write(going_out)
    #print "Sent outgoing stuff woohoo!"
    if(part2):
        #print "Processing a command"
        to_process = getlinesuntil(part2, getline, linelen_atleast, 3)
        assert to_process[0]=="\x00"
        the_dom = G.DOMDICT[ord(to_process[1])][1] #Remember, items stored in DOMDICT as (ver, domain)
        the_func = the_dom[to_process[2]]
        the_regex = re.compile(the_func.regex + r"\n\Z", re.S)
        #print repr(the_func.regex)
        #print "Got the dom, the func, the regex"
        #print repr(to_process)
        remainder = to_process[3:]
        #print remainder
        #print the_regex.match(remainder)
        argstring = getlinesuntil(remainder, getline, the_regex.match)
        argtuple = the_regex.findall(argstring)[0] #Remember, findall==list of tuples
        if(G.SEEINTERNAL):
            print "Giving function: " + repr(argtuple)
        send(the_func(the_domain, argtuple))

