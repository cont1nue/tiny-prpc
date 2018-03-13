'''
the demo server of the tiny prpc framework.
'''
from src import argument_check
from src import PrpcServer

@argument_check((int, float), (int, float))
def add(x, y):
    return x + y

@argument_check((int, float), (int, float))
def div(x, y):
    return x / y

class test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

@argument_check((int, float), (int, float))
def test_class(x, y):
    return test(x, y)

@argument_check(int, dict)
def dict_test(x, y):
    y[x] = 1
    return y



if __name__ == "__main__":
    prpcserver = PrpcServer("127.0.0.1", 8080)
    prpcserver.service_register("add", add)
    prpcserver.service_register("test_class", test_class)
    prpcserver.service_register("div", div)
    prpcserver.service_register("dict_test", dict_test)
    prpcserver.start()



