class FdDict(dict):
    def append(self, thing):
        self[sorted(list(set(range(0,256)) - set(self.keys())))[0]] = thing
        
class PSOXFd(object):
    def out_absseek(self, num):
        raise NotImplementedError
    def in_absseek(self, num):
        raise NotImplementedError
    def out_relseek(self, num):
        raise NotImplementedError
    def in_relseek(self, num):
        raise NotImplementedError
    def in_flush(self):
        raise NotImplementedError
    def out_flush(self):
        raise NotImplementedError
    def in_close(self):
        raise NotImplementedError
    def out_close(self):
        raise NotImplementedError
        
    def write(self, stuff):
        raise NotImplementedError
    def read(self, bytes):
        raise NotImplementedError
        
        
class FdWrapper(PSOXFd):
    def __init__(self, infile = None, outfile = None):
        if infile is not None:
            self.infile = infile
        if outfile is not None:
            self.outfile = outfile
    
    def out_absseek(self, num):
        if(num>=0):
            self.outfile.seek(num, 0)
        else:
            self.outfile.seek(num, 2)
    def in_absseek(self, num):
        if(num>=0):
            self.infile.seek(num, 0)
        else:
            self.infile.seek(num, 2)
        
    def out_relseek(self, num):
        self.outfile.seek(num, 1)
    def in_relseek(self, num):
        self.infile.seek(num, 1)
        
    def out_flush(self):
        self.outfile.flush()
    def in_flush(self):
        self.infile.flush()
    def out_close(self):
        self.outfile.close()
    def in_close(self):
        self.infile.close()
    
    def write(self, text):
        self.outfile.write(text)
    def read(self, bytes):
        if(not bytes):
            return self.infile.readline()
        else:
            return self.infile.read(bytes)
      
      
import sys
STDFD = FdWrapper(infile = sys.stdin, outfile = sys.stdout)
