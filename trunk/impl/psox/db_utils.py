from domain import Domain, argtypes, rettypes
from psoxtypes import FNUM, FBYTES, STRING, LNUM, LBYTES

PSOX_VERSION = (0, 0, 0)
MY_VERSION = 1

class MyDomain(Domain):
    
    @argtypes(FNUM(1), STRINGNL)
    @rettypes(FNUM(1))
    def f00(self, base, string):
        return int(string, base)
        
    @argtypes(FNUM(1), STRINGNL)
    @rettypes(LNUM)
    def f01(self, base, string):
        return int(string, base)
        
    @argtypes(FNUM(1), FNUM(1))
    @rettypes(STRING)
    def f02(self, base, num):
        if(base==8):
            return oct(num)
        elif(base==10):
            return str(num)
        elif(base==16):
            return hex(num)
        else:
            raise NotImplementedError
    
    @argtypes(FNUM(1), LNUM)
    @rettypes(STRING)
    def f03(self, base, num):
        if(base==8):
            return oct(num)
        elif(base==10):
            return str(num)
        elif(base==16):
            return hex(num)
        else:
            raise NotImplementedError  
            
    @argtypes(FNUM(1))
    @rettypes(FNUM(1))
    def f04(self, byte):
        return int(not byte)
        
    @argtypes(FNUM(1))
    @rettypes(FNUM(1))
    def f05(self, byte):
        return (byte ^ 0xFF)
        
    @argtypes(FNUM(1), FNUM(1))
    @rettypes(FNUM(1))
    def f06(self, b1, b2):
        return int(b1 and b2)
        
    @argtypes(FNUM(1), FNUM(1))
    @rettypes(FNUM(1))
    def f07(self, b1, b2):
        return int(b1 & b2)
        
    @argtypes(FNUM(1), FNUM(1))
    @rettypes(FNUM(1))
    def f08(self, b1, b2):
        return int(b1 or b2)
        
    @argtypes(FNUM(1), FNUM(1))
    @rettypes(FNUM(1))
    def f09(self, b1, b2):
        return int(b1 | b2)
        
    @argtypes(FNUM(1), FNUM(1))
    @rettypes(FNUM(1))
    def f0A(self, b1, b2):
        return int((b1 or b2) and not (b1 and b2))
    
    @argtypes(FNUM(1), FNUM(1))
    @rettypes(FNUM(1))
    def f0B(self, b1, b2):
        return int(b1 ^ b2)
        
    @argtypes(FNUM(1), FNUM(1))
    @rettypes(FNUM(1))
    def f0C(self, n1, n2):
        return n1 + n2
    
    @argtypes(LNUM, LNUM)
    @rettypes(LNUM)
    def f0D(self, n1, n2):
        return n1 + n2

    @argtypes(FNUM(1), FNUM(1))
    @rettypes(FNUM(1))
    def f0E(self, n1, n2):
        return n1 - n2
    
    @argtypes(LNUM, LNUM)
    @rettypes(LNUM)
    def f0F(self, n1, n2):
        return n1 - n2
        
    @argtypes(FNUM(1), FNUM(1))
    @rettypes(FNUM(1))
    def f10(self, n1, n2):
        return n1 * n2
    
    @argtypes(LNUM, LNUM)
    @rettypes(LNUM)
    def f11(self, n1, n2):
        return n1 * n2
        
    @argtypes(FNUM(1), FNUM(1))
    @rettypes(FNUM(1))
    def f12(self, n1, n2):
        return n1 / n2
    
    @argtypes(LNUM, LNUM)
    @rettypes(LNUM)
    def f13(self, n1, n2):
        return n1 / n2
        

