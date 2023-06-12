#!/usr/bin/env python

import socket
import struct

TCP_IP = '127.0.0.1'
TCP_PORT = 54321
MESSAGE = struct.pack("<i13s", 13, b'Hello world!!')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket
s.connect((TCP_IP, TCP_PORT)) # connect to local host on unused port
s.send(MESSAGE)

length = s.recv(4) # length of succeeding message
length = int.from_bytes(length, "little") # convert bytes object to int
data = s.recv(length)
data = data.decode("utf-8") # convert bytes object to string
print("Message from Server:", data)

# clean up
s.close()