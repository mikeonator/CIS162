# CIS162 - Week7 - Michael Audi Client Program

import socket

HOST = '127.0.0.1'    # The remote host
PORT = 42069        # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(f'Hello, {s.getsockname()}, I am the Client!'.encode('utf-8'))
    data = s.recv(1024)
print('Received from server:', repr(data))
