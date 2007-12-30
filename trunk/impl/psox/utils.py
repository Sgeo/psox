def getlines(getline, func, *args, **kwargs):
    """repeatedly calls getline() until the concatination of getline() makes func(the_concat, *args, **kwargs) True."""
    the_line = ""
    while(not (func(the_line, *args, **kwargs))):
        the_line += getline()
    return the_line
    
def linelen(string, length):
    if(len(string) < length):
        return False
    elif(len(string) > length):
        from psox.errors import IllegalPSOXError
        raise IllegalPSOXError
    return True
    
def vn2vs(major, minor1, minor2 = None):
    if(minor2 is not None):
        append = "-" + str(minor2)
    else:
        append = ""
    if(type(minor1)==tuple):
        minor1 = str(minor1[0]) + "-" + str(minor1[1])
    return str(major) + "." + str(minor1) + append
    
