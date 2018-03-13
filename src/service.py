'''
define the rpc processing logic
'''
import pickle
from .exception import FunctionNotExistError

class Service:
    '''
    parsing the client data and call the functions
    '''
    def __init__(self):
        self._function_dict = {}
    
    def register(self, function_name, function):
        '''
        register the function into function dict
        '''
        self._function_dict[function_name] = function

    def call(self, function_name, *params):
        '''
        call the functions with giving params
        '''
        try:
            if function_name not in self._function_dict:
                return FunctionNotExistError("the function not in the service")
            return self._function_dict[function_name](*params)
        except Exception as e:
            return e

    def result_pack(self, data):
        '''
        packing the result and send back to the client
        '''
        if isinstance(data, Exception):
            return pickle.dumps({"error": str(data)})
        else:
            return pickle.dumps({"result": data})

    def run(self, unpacked_data):
        '''
        unpack the client data and call the functions
        '''
        packed_data = pickle.loads(unpacked_data)
        function_name, params = packed_data["function_name"], packed_data["params"]
        call_output = self.call(function_name, *params)
        return self.result_pack(call_output)
