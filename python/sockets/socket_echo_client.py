#!/usr/bin/python
#original_source - http://pymotw.com/2/socket/tcp.html

import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    # Send data
    num=0;
    while(1):
        message = str(num) + ';event;start;timelinescene\n'
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(message)
        time.sleep(1)
        num = num+1
        message2 = str(num) + ';event;stop;timelinescene\n'
        sock.sendall(message2)
        num = num+0.5

    # Look for the response
    #amount_received = 0
    #amount_expected = len(message)
    
    #while amount_received < amount_expected:
    #    data = sock.recv(16)
    #    amount_received += len(data)
    #    print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()



