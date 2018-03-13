# tiny-prpc
a tiny python rpc framework.

# demo
you can reference to the client_demo.py and server_demo.py

# intro
this is a tiny python rpc framework, base on the epoll I/O framework.

# usage

**When you using this rpc framework, you can use the argument_check decorator in function define.**

**Server Code**

```python
from src import PrpcServer
from src import argument_check

class test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

@argument_check((int, float), (int, float))
def test_class(x, y):
    return test(x, y)

@argument_check((int, float), (int, float))
def add(x, y):
    return x+y

prpcserver = PrpcServer("127.0.0.1", 8080)
prpcserver.service_register("add", add)
prpcserver.service_register("test_class", test_class)
prpcserver.start()
```

**Client Code**

```python
from src import PrpcClient

prpcclient = PrpcClient("127.0.0.1", 8080)
prpcclient.run(add, [1, 2])
```
**If you want get object result in this rpc frame work, you must define the class  in the client**
```python
from src import PrpcClient

class test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

prpcclient = PrpcClient("127.0.0.1", 8080)
prpcclient.run("test_class", [1, 2])
```


