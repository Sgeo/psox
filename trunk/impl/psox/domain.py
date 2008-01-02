#from functools import wraps #Note: Python 2.5

def argtypes(*types):
    def f(func):
        #@wraps
        def g(self, *args, **kwargs):
            processed_args = tuple(i.fromtype(j) for (i,j) in zip(types, args))
            return func(self, *processed_args, **kwargs)
        g.regex = ''.join(i.regex for i in types)
        return g
    return f

def rettypes(*types):
    def f(func):
        #@wraps #Needed to keep __name__ sane
        def g(self, *args, **kwargs):
            returned = func(self, *args, **kwargs)
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
            def f(*args, **kwargs):
                return v(self, *args, **kwargs)
            f.regex = v.regex
            self.f_dict[chr(int(k[1:], 16))] = f
            
    def __getitem__(self, key):
        """Remember, the key is a char, not a num"""
        return self.f_dict[key]
