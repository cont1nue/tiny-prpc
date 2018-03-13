'''
define the exception of the error in the rpc framework.
'''

class ArgumentLengthError(Exception):
    '''
    define the argument length error in the type decorator
    '''
    pass

class ArgumentTypeError(Exception):
    '''
    define the arugment type error in the type decorrator.
    '''
    pass

class FunctionNotExistError(Exception):
    '''
    define the function not exist error in the function call.
    '''
    pass