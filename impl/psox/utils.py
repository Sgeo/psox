def getlinesuntil(the_line, getline, func, *args, **kwargs):
    """repeatedly calls getline() until the concatination of getline() makes func(the_concat, *args, **kwargs) True."""
    while(not (func(the_line, *args, **kwargs))):
        the_line += getline()
    return the_line
    
def linelen(string, length):
    if(len(string) < length):
        return False
    elif(len(string) > length):
        from psox.errors import IllegalPSOXError
        raise IllegalPSOXError("Expected length of " + str(length) + ", got length " + str(len(string)) + " with string " + repr(string))
    return True
    
    
def linelen_atleast(string, length):
    if(len(string) < length):
        return False
    return True
    
def vn2vs(major, minor1, minor2 = None):
    if(minor2 is not None):
        append = "-" + str(minor2)
    else:
        append = ""
    if(type(minor1)==tuple):
        minor1 = str(minor1[0]) + "-" + str(minor1[1])
    return str(major) + "." + str(minor1) + append
    
def bin(num):
    """Stolen from bz2 of Sine"""
    b=""
    while num > 0:
        b = str(num%2) + b
        num = num/2
    return b
    
def pack(num):
    """Much thanks to KirkMcDonald of #python"""
    parts = []
    while num:
        parts.append(num & 0xFF)
        num >>= 8
    return ''.join(chr(i) for i in reversed(parts))

def unpack(data):
    result = 0
    while data:
        result <<= 8
        result += ord(data[0])
        data = data[1:]
    return result
    
