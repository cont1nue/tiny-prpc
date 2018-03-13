'''
define the type assert decorator
'''
from .exception import ArgumentLengthError, ArgumentTypeError

def argument_check(*types):
    def check(f):
        if len(types) != f.__code__.co_argcount:
            raise ArgumentLengthError("type length is not same with function argument count!")
        def new_f(*args, **kwds):
            for(arg, check_type) in zip(args, types):
                if not isinstance(arg, check_type):
                    raise ArgumentTypeError("the type is not match!")
            return f(*args, **kwds)
        new_f.__name__ = f.__name__
        return new_f
    return check