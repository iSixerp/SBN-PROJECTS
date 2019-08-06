from socket import socket, AF_INET, SOCK_DGRAM
DEFAULT_ADDRESS = ('127.0.0.1', 11111)

class Client():
    '''
    Simple client written in Python3. Polls a server and waits for its response.
    '''
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind(('127.0.0.1', 11112)) # OS chooses port
        self.socket_name = self.socket.getsockname()
    
    def poll_server(self, data, server=DEFAULT_SERVER):
        self.socket.sendto(bytes(data, "utf-8"), server)
        response, addr = self.socket.recvfrom(1022)
        self.socket.close()
        return response, addr


if __name__ == '__main__':
    test_client = Client()
    print(test_client.poll_server("Hello world"))