def argtypes(*args):
    def f(func):
        func.regex = ''.join(i.regex for i in args)
        return func
    return f

def rettypes(*types):
    def f(func):
        def g(*args, **kwargs):
            returned = func(*args, **kwargs)
            if(type(returned)!=tuple):
                returned = (returned,)
            assert len(types)==len(returned)
            return ''.join(i.totype(j) for (i, j) in zip(types, returned))
        return g
    return f

class Domain(object):
    def __init__(self):
        self.f_dict = {}
        funcs = [i for i in self.__class__.__dict__ if i.__name__[0]=="f" and len(i.__name__)==3]
        for i in funcs:
            self.f_dict[chr(int(i.__name__[1:], 16))] = i
            
    def __getitem__(self, key):
        """Remember, the key is a char, not a num"""
        return self.f_dict[key]
