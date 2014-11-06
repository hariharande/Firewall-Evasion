__author__ = 'dkay'
#! /usr/bin/python
import socket
import sys
import json

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (('localhost' ,2002))
print ("Starting up on %s port %s", server_address)
sock.connect(server_address)

try:

    # Send data
    message1 = '{"command" : "AUT'
    message2 = 'H", "user" : "paperliteral"}'
    message4 = json.loads(message1+message2)
    print message4
    #print >>sys.stderr, 'sending %s' % message1 + message2
    sock.sendall(message1+message2)
    #sock.sendall(message2)
    ####LOOK FOR THE RESPONSE####
    amount_received = 0
    #amount_expected = len(message)

    #while amount_received < amounmount_expected = len(message)t_expected:
    data = sock.recv(1024)
    amount_received += len(data)
    print >>sys.stderr, 'received %s' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
