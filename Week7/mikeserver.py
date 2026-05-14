# CIS162 - Week7 - Michael Audi Server Program

import socket

HOST = '127.0.0.1'
PORT = 42069

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f'Received from ({addr}):', repr(data))
            conn.sendall(f'Hello, {addr}, I am the server!'.encode('utf-8'))
