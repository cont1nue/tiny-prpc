'''
the server of the rpc framework.
'''
import socket
import select
from .log import logging
from .service import Service
from .utils import recvall


class PrpcServer:
    '''
    the prpc server code
    '''
    def __init__(self, ip, port):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((ip, port))
        self._socket.listen(1)
        self._socket.setblocking(0)
        self._buffer_size = 1024
        self._epoll = select.epoll()
        self._epoll.register(self._socket.fileno(), select.EPOLLIN)
        self._fd_to_socket = {self._socket.fileno():self._socket}
        self._requests = {}
        self._service = Service()

    def service_register(self, function_name, function):
        '''
        register the service rpc functions
        '''
        self._service.register(function_name, function)

    def start(self):
        '''
        start the epoll events.
        '''
        while True:
            events = self._epoll.poll(-1)
            for fd, event in events:
                socket = self._fd_to_socket[fd]
                if socket == self._socket:
                    conn, add = self._socket.accept()
                    logging.info("accpet a new connection %s:%d from the client", add[0], add[1])
                    conn.setblocking(0)
                    self._epoll.register(conn.fileno(), select.EPOLLIN)
                    self._fd_to_socket[conn.fileno()] = conn
                elif event & select.EPOLLIN:
                    data = recvall(socket, self._buffer_size)
                    if data == b"":
                        self._epoll.unregister(fd)
                        self._fd_to_socket[fd].close()
                        del self._fd_to_socket[fd]
                        continue
                    self._requests[fd] = self._service.run(data)
                    self._epoll.modify(fd, select.EPOLLOUT)
                elif event & select.EPOLLOUT:
                    socket.send(self._requests[fd])
                    self._epoll.modify(fd, select.EPOLLIN)



                    
    