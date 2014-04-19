__author__ = 'michaelluo'

import socket

HOST = '54.86.52.137'    # The remote host
PORT = 5069              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)