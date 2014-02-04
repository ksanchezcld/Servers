'''
From Python for Hackers - Networkers Primer
http://www.youtube.com/watch?v=3JeHWl0cjJ8
'''
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('localhost', 9252)
print 'starting up on %s port %s' % server_address
s.bind(server_address)
s.listen(4)
connection, client_address = s.accept()
print 'connection from', connection.getpeername()
data = connection.recv(4096)
if data:
	print 'received', repr(data)
	data = data.rstrip()
	connection.send("%s\n%s\n%s\n" % ('-'*80, data.center(80), '-'*80))
	print "Response sent!"

connection.shutdown(socket.SHUT_RD | socket.SHUT_WR)
connection.close()
print "Conection close!"
s.close()
