def argtypes(*args):
    def f(func):
        func.regex = ''.join(i.regex for i in args)
        return func
    return f

def rettypes(*types):
    def f(func):
        def g(*args, **kwargs):
            returned = f(*args, **kwargs)
            if(type(returned)!=tuple):
                returned = (returned,)
            assert len(types)==len(returned)
            return ''.join(i.totype(j) for (i, j) in zip(types, returned))
        return g
    return f

class Domain(object):
    def __init__(self):
        
