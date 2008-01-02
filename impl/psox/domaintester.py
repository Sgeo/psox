from domain import argtypes, rettypes, Domain
from psoxtypes import FNUM, LNUM, STRING, LBYTES

class TestDomain(Domain):
    @argtypes(LNUM)
    @rettypes(STRING)
    def f00(self, num):
        return str(num+1)
    @argtypes(FNUM(2))
    @rettypes(STRING)
    def f01(self, num):
        return str(num)
        
        
the_domain = TestDomain()
print the_domain['\x00'].regex
print repr(the_domain['\x00'](the_domain, "\x01\x01\x01\x01\x00", "Hello!\x00"))
#print repr(
#print the_domain['\x00'].regex
print the_domain['\x01'].regex
print repr(the_domain['\x01'](the_domain, "\x01\x01"))
