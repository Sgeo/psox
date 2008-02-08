from domain import Domain, argtypes, rettypes
from psoxtypes import STRING, LBYTES, LNUM, FNUM, VARG, FBYTES
import psoxglobals as G

MY_VERSION = 1

class SysDomain(Domain):

    @argtypes(LNUM)
    @rettypes(STRING)
    def f00(self, num):
        """Just an example function, not spec"""
        return str(num)
    
    @argtypes(FNUM(1))
    @rettypes()
    def f01(self, status):
        from sys import exit
        exit(status)
        
    @argtypes(FNUM(1))
    @rettypes(FNUM(1))
    def f02(self, domnum):
        if(domnum in G.DOMDICT):
            return G.DOMDICT[domnum](0)
        else:
            return 0
    
    @argtypes()
    @rettypes(STRING)
    def f04(self):
        return G.CLINE
        
    @argtypes(STRING)
    @rettypes(FNUM(1))
    def f06(self, somestring):
        return int(somestring in G.SAFETYLIST)
        
    @argtypes()
    @rettypes(STRING)
    def f08(self):
        return "PSOX.py"
        
    @argtypes(FNUM(1))
    @rettypes()
    def f10(self, some_fd):
        G.FDDICT[0] = G.FDDICT[some_fd]
        
    @argtypes(FNUM(1))
    @rettypes()
    def f11(self, some_fd):
        G.FDDICT[1] = G.FDDICT[some_fd]
        
    @argtypes(FNUM(1), LNUM)
    @rettypes()
    def f12(self, some_fd, seek):
        G.FDDICT[some_fd].absseek(seek)
        
    @argtypes(FNUM(1), LNUM)
    @rettypes()
    def f13(self, some_fd, seek):
        G.FDDICT[some_fd].relseek(seek)
        
    @argtypes(FNUM(1))
    @rettypes()
    def f14(self, some_fd):
        G.FDDICT[some_fd].flush()
        
    @argtypes(FNUM(1))
    @rettypes()
    def f15(self, some_fd):
        G.FDDICT[some_fd].close()
        
    @argtypes(FNUM(1))
    @rettypes()
    def f15(self, some_fd):
        the_fd = G.FDDICT[some_fd]
        if G.FDDICT[0] is some_fd:
            G.FDDICT[0] = G.FDDICT[2]
        if G.FDDICT[1] is some_fd:
            G.FDDICT[1] = G.FDDICT[3]
        G.FDDICT[some_fd].close()
        
        
        
the_domain = SysDomain
