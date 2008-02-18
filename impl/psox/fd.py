import psoxglobals as G

class FdDict(dict):
    def append(self, thing):
        self[sorted(list(set(range(0,256)) - set(self.keys())))[0]] = thing
        
        
class PSOXFd(object):
    def absseek(self, num):
        raise NotImplementedError
    def relseek(self, num):
        raise NotImplementedError
    def flush(self):
        raise NotImplementedError
    def close(self):
        raise NotImplementedError        
    def write(self, stuff):
        raise NotImplementedError
    def read(self, bytes):
        raise NotImplementedError
        
        
class FdWrapper(PSOXFd):
    def __init__(self, filelike):
        self.filelike = filelike    
    def absseek(self, num):
        if(num>=0):
            self.filelike.seek(num, 0)
        else:
            self.filelike.seek(num, 2)        
    def relseek(self, num):
        self.filelike.seek(num, 1)     
    def flush(self):
        self.filelike.flush()
    def close(self):
        self.filelike.close()
    
    def write(self, text):
        self.filelike.write(text)
    def read(self, bytes):
        if(not bytes):
            return self.filelike.readline()
        else:
            return self.filelike.read(bytes)
      
      
import sys
STDIN_FD = FdWrapper(sys.stdin)
STDOUT_FD = FdWrapper(sys.stdout)
G.FDDICT = FdDict()
G.FDDICT[2] = STDOUT_FD
G.FDDICT[3] = STDIN_FD
G.FDDICT[0] = STDOUT_FD
G.FDDICT[1] = STDIN_FD
#Code throughout the project should generally write to G.FDDICT[0] and read from G.FDDICT[1]
#Changing the current FDs is simply assigning to G.FDDICT[0] and/or G.FDDICT[1]
