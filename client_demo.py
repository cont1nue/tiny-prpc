'''
the demo client of the tiny prpc framework.
'''
from src import PrpcClient

class test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

prpcclient = PrpcClient("127.0.0.1", 8080)


add_result = prpcclient.run("add", [1, 2])
add_err_result = prpcclient.run("add", [1, "2"])
class_result = prpcclient.run("test_class", [1, 2])
div_result = prpcclient.run("div", [1, 0])
div_err_result = prpcclient.run("div", [1, 2])
dict_result = prpcclient.run("dict_test", [1, {"hello":"world"}])
dict_err_result = prpcclient.run("dict_test1", [1, {"hello":"world"}, 3])

print(add_result)
print(add_err_result)
print(class_result)
print(div_result)
print(div_err_result)
print(dict_result)
print(dict_err_result)