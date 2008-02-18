from domain import Domain, argtypes, rettypes
from psoxtypes import STRINGNL
import psoxglobals as G
from fd import FdWrapper
import urllib2 as url

class HTTPDomain(Domain):
    
    @argtypes(STRINGNL)
    @rettypes()
    def f00(self, the_url):
        G.FDDICT.append(url.urlopen(the_url))
        
the_domain = HTTPDomain
