from domain import argtypes, rettypes, Domain
from psoxtypes import LNUM, STRING

class TestDomain(Domain):
    @argtypes(LNUM)
    @rettypes(STRING)
    def f00(self, num):
        return str(num+1)
        
        
the_domain = TestDomain()
print the_domain['\x00']("\x01\x01\x00")
