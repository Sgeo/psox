from domain import Domain, argtypes, rettypes
from psoxtypes import FNUM, STRING, STRINGNL
import psoxglobals as G
from fd import FdDict, PSOXFd, FdWrapper #FdDict is used for storing the server sockets
import urllib2 as url

ServerSockets = FdDict()

class FdSocketWrapper(PSOXFd):
    def __init__(self, socket_obj):
        self.socket = socket_obj
    def write(self, stuff):
        self.socket.sendall(stuff)
    def read(self, bytes):
        if(bytes):
            return self.socket.recv(bytes)
        else:
            lastbyte = ""
            the_bytes = ""
            while lastbyte != "\n":
                lastbyte = self.socket.recv(1)
                the_bytes += lastbyte
            return the_bytes
    def close(self):
        self.socket.close()

MY_VERSION = 1

class NetDomain(Domain):
    
    @argtypes(FNUM(1), FNUM(2), STRINGNL)
    @rettypes()
    def f00(self, tcp_or_udp, port, addr):
        if tcp_or_udp:
            SOCK = socket.SOCK_DGRAM
        else:
            SOCK = socket.SOCK_STREAM
        
        s = socket.socket(socket.AF_INET, SOCK)
        s.connect((addr, port))
        G.FDDICT.append(FdSocketWrapper(s))
        
    @argtypes(FNUM(1), FNUM(1), FNUM(2), STRINGNL)
    @rettypes()
    def f01(self, backlog, tcp_or_udp, port, addr):
        if tcp_or_udp:
            SOCK = socket.SOCK_DGRAM
        else:
            SOCK = socket.SOCK_STREAM
            
        s = socket.socket(socket.AF_INET, SOCK)
        s.bind((addr, port))
        s.listen(backlog)
        ServerSockets.append(s)
        
    @argtypes(FNUM(1))
    @rettypes(STRING)
    def f02(self, the_serversocket):
        s = ServerSockets[the_serversocket]
        conn, addr = s.accept()
        G.FDDICT.append(conn)
        return addr
        
    @argtypes(FNUM(1))
    @rettypes()
    def f03(self, the_serversocket):
        del ServerSockets[the_serversocket]
        
    @argtypes(STRINGNL)
    @rettypes()
    def f04(self, the_url):
        G.FDDICT.append(url.urlopen(the_url))
        
    @argtypes(STRING, STRINGNL)
    @rettypes()
    def f05(self, the_url, postdata):
        G.FDDICT.append(url.urlopen(the_url, postdata))
        
        
the_domain = NetDomain
