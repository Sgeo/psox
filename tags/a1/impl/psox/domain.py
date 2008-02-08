#from functools import wraps #Note: Python 2.5

from psoxglobals import SEEINTERNAL

def argtypes(*types):
    def f(func):
        #@wraps
        def g(self, *args, **kwargs):
            if(SEEINTERNAL): print "@argtypes sees: " + repr(args)
            processed_args = tuple(i.fromtype(j) for (i,j) in zip(types, args))
            if(SEEINTERNAL): print "@argtypes sent: " + repr(processed_args)
            return func(self, *processed_args, **kwargs)
        g.regex = ''.join(i.regex for i in types)
        return g
    return f

def rettypes(*types):
    def f(func):
        #@wraps #Needed to keep __name__ sane
        def g(self, *args, **kwargs):
            returned = func(self, *args, **kwargs)
            if(returned is None):
                return ""
            if(type(returned)!=tuple):
                returned = (returned,)
            assert len(types)==len(returned)
            return ''.join(i.totype(j) for (i, j) in zip(types, returned))
        return g
    return f

class Domain(object):
    def __init__(self):
        self.f_dict = {}
        funcs = [(k, v) for (k, v) in self.__class__.__dict__.items() if k[0]=="f" and len(k)==3]
        for k, v in funcs:
            self.f_dict[chr(int(k[1:], 16))] = v
            
            
    def __getitem__(self, key):
        """Remember, the key is a char, not a num. Also, you need to pass the domain itself into the function manually :("""
        return self.f_dict[key]

