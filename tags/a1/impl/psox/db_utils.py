from domain import Domain, argtypes, rettypes
from psoxtypes import FNUM, FBYTES, STRING, LNUM, LBYTES

PSOX_VERSION = (0, 0, 0)
MY_VERSION = 1

class MyDomain(Domain):
    
    @argtypes(FNUM(1))
    @rettypes(STRING)
    def f01(self, num):
        return str(num)
        
    @argtypes(LNUM)
    @rettypes(STRING)
    def f02(self, num):
        return str(num)
