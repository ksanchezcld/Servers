import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9252))
s.send('Happy Hacking')
data = s.recv(1024)
s.close
print 'Received'
print data
