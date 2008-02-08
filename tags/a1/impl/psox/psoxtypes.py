from utils import pack, unpack
import re
import psoxglobals as G
class PSOXType(object):
        
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
        if(G.SEEINTERNAL):
            print "The type sees: " + repr(stuff)
            print "Function sees: " + repr(unpack(stuff))
        return unpack(stuff)
        
        
class FBYTES(PSOXType):
    def __init__(self, size):
        self.size = size
        self.regex = r"(.{" + str(size) + r"})"
    
    def totype(self, stuff):
        stuff = str(stuff)
        assert len(stuff) <= self.size
        return "\x00" * (self.size - len(stuff)) + stuff
    
    def fromtype(self, stuff):
        if(G.SEEINTERNAL):
            print "Function sees: " + str(ord(stuff))
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
        result = header + result + "\x00"
        return result
        
    def fromtype(self, stuff):
        result = unpack(stuff[1:-1:2])
        if(stuff[0]=="\x02"):
            result *= -1
        return result
        
LNUM = LNUM()

class LBYTES(PSOXType):
    regex = r"((?:\x02.)?(?:\x01.)*?\x00)"
    
    def totype(self, stuff):
        stuff = str(stuff)
        return "\x01" + '\x01'.join(list(stuff)) + "\x00"
        
    def fromtype(self, stuff):
        return stuff[1:-1:2]
        
LBYTES = LBYTES()

class VARG(PSOXType):
    
    def __init__(self, a_type):
        self.the_type = a_type
        self.regex = r"((?:\x01(?:" + a_type.regex[1:-1] + r"))*?\x00)" #Note that the regexes of all types have () on both sides
        fromtype_regex = r"\x01" + a_type.regex
        self.comp_regex = re.compile(fromtype_regex, re.S)
        
    def totype(self, stuff):
        if((not hasattr(stuff, "__iter__")) or isinstance(stuff, basestring)):
            stuff = (stuff,)
        return "\x01" + "\x01".join(self.the_type.totype(i) for i in stuff) + "\x00"
        
    def fromtype(self, stuff):
        return tuple(self.the_type.fromtype(i) for i in self.comp_regex.findall(stuff))
        
class REGEX(PSOXType):
    def __init__(self, a_regex, totype=None, fromtype=None):
        self.regex = a_regex
        if totype is not None:
            self.totype = totype
        if fromtype is not None:
            self.fromtype = fromtype
        
