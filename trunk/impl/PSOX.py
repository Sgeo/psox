PSOX_MAJOR_VER = 0
PSOX_MINOR_VER_RANGE = (0, 0)

from optparse import OptionParser
from subprocess import Popen, PIPE
import sys

parser = OptionParser(usage="%prog [-s safety1,safety2] [-c \"fakecommandline\"] command", version="PSOX 0.0 - %prog 0.0")
parser.add_option("-s", "--safety", dest="safety", help="Specifies safety options. e.g to allow full access to the filesystem, and no Internet access, use \"-s fullfileio,nonet\"")
parser.add_option("-c", "--command-line", dest="cline", help="Specifies the virtual command line for the client")

options, args = parser.parse_args()

client = Popen(args, stdin=PIPE, stdout=PIPE)

curline = client.stdout.readline()
if(len(curline)!=4):
    print "Not valid PSOX"
    sys.exit(1)
elif(curline[0:2]!="\x00\x07"):
    print "Not valid PSOX"
    sys.exit(1)
elif(curline[2] != chr(PSOX_MAJOR_VER)):
    print "Wrong PSOX version"
    sys.exit(1)
else:
    print "Checking minor ver not implemented yet"
