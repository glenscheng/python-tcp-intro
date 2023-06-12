#!/usr/bin/env python

import socket
import struct

TCP_IP = '127.0.0.1'
TCP_PORT = 54321
RESPONSE = struct.pack("<i32s", 32, b'Data has been received by Server')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket
s.bind((TCP_IP, TCP_PORT)) # bind socket to localhost and unused port
s.listen(1) # become a server socket by waiting for 1 client to connect

conn, addr = s.accept() # accept connections from outside
while True:
    length = conn.recv(4) # length of succeeding message
    length = int.from_bytes(length, "little") # convert bytes object to int
    data = conn.recv(length)
    data = data.decode("utf-8") # convert bytes object to string
    if not data: break
    print("Message from Client:", data)
    conn.send(RESPONSE)

# clean up
conn.close()
s.close()