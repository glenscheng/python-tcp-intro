# python-tcp-intro
2 small python programs where a client and server send each other packets of the following contents: 
<br>4-byte length | string payload of the prefixed length
 
# Goal
* Create two python programs, client and server
* The client sends a message of the above format
* The server gets the payload, prints it to screen and replies with a message of the above format
* The client receives the payload and prints it to screen
* Both programs exit, closing their sockets

# Instructions
1. Run `python3 socket_server.py` script in one window
2. Run `python3 socket_client.py` script in another window
3. Scripts print to screens

# Resources
* encoding/decoding binary data: https://docs.python.org/3/library/struct.html
* bytes objects: https://docs.python.org/3/library/stdtypes.html#bytes-objects
* TCP sockets HOW TO: https://docs.python.org/3/howto/sockets.html
* sockets interface: https://docs.python.org/3/library/socket.html
* TCP sockets example: https://wiki.python.org/moin/TcpCommunication
* ports info: https://www.sciencedirect.com/topics/computer-science/registered-port#:~:text=Between%20the%20protocols%20User%20Datagram,ports%3A%20Range%20from%200%E2%80%931%2C023
