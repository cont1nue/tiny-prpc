'''
the client of the rpc framework.
'''
import socket
import pickle
from .utils import recvall

class PrpcClient:
    '''
    the prpc client code
    '''
    def __init__(self, ip, port):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((ip, port))
        self._buffer_size = 1024

    def create_packed_data(self, function_name, params_list):
        '''
        create the bytes data using pickle
        '''
        return pickle.dumps({"function_name": function_name, "params": params_list})


    def run(self, function_name, params_list):
        '''
        run the function with the function name and params
        '''
        packed_data = self.create_packed_data(function_name, params_list)
        self._socket.send(packed_data)
        packed_data = recvall(self._socket, self._buffer_size)
        return pickle.loads(packed_data)

