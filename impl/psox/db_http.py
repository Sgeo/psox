from domain import Domain, argtypes, rettypes
from psoxtypes import STRINGNL
import psoxglobals as G
from fd import FdWrapper
import urllib2 as url

if "nonet" in G.SAFETYLIST or "nohttp" in G.SAFETYLIST:
    MY_VERSION = 0
else:
    MY_VERSION = 1
    
class HTTPDomain(Domain):
    
    @argtypes(STRINGNL)
    @rettypes()
    def f00(self, the_url):
        G.FDDICT.append(url.urlopen(the_url))
        
the_domain = HTTPDomain
