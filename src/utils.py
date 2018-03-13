'''
define the util function or class using in the project.
'''

def recvall(socket, buffer_size):
    '''
    recv all data from the socket
    '''
    data = b""
    while True:
        part = socket.recv(buffer_size)
        data += part
        if len(part) < buffer_size:
            break
    return data