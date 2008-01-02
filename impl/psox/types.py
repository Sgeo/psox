from utils import pack, unpack
class PSOXType(object):
    def __init__(self):
        pass
        
    def totype(self, stuff):
        raise NotImplementedError
    
    def fromtype(self, stuff):
        raise NotImplementedError
        
    regex = r""
    
class FNUM(PSOXType):
    def __init__(self, size):
        self.size = size
        self.regex = r"(.{" + str(size) + r"})"
    
    def totype(self, num):
        num = int(num)
        assert num >= 0
        result = pack(num)
        len_result = len(result)
        assert len_result <= self.size
        result = "\x00" * (self.size - len_result) + result
        return result
        
    def fromtype(self, stuff):
        return unpack(stuff)
        
        
class FBYTES(PSOXType):
    def __init__(self, size):
        self.size = size
        self.regex = r"(.{" + str(size) + r"})"
    
    def totype(self, stuff):
        assert len(stuff) <= self.size
        return "\x00" * (self.size - len(stuff)) + stuff
    
    def fromtype(self, stuff):
        return stuff
        

class STRING(PSOXType):
    regex = r"([^\x00]*?\x00)"
    
    def totype(self, stuff):
        stuff = str(stuff)
        assert "\x00" not in stuff
        return stuff + "\x00"
        
    def fromtype(self, stuff):
        assert stuff[-1]=="\x00" and "\x00" not in stuff[:-1]
        return stuff[:-1]
        
STRING = STRING()

class LNUM(PSOXType):
    regex = r"((?:\x02.)?(?:\x01.)*?\x00)"
    
    def totype(self, num):
        num = int(num)
        result = '\x01'.join(i for i in pack(num))
        if num >= 0:
            header = "\x01"
        else:
            header = "\x02"
        result = header + result + "\x00
        return result
        
    def fromtype(self, stuff):
        return unpack(stuff[1:-1:2])
        
LNUM = LNUM()

class LBYTES(PSOXType):
    regex = r"((?:\x02.)?(?:\x01.)*?\x00)"
    
    def totype(self, stuff):
        stuff = str(stuff)
        return "\x01" + '\x01'.join(list(stuff)) + "\x00"
        
    def fromtype(self, stuff):
        return stuff[1:-1:2]
        
