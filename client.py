# client.py
import socket

# get local machine name
#host = socket.gethostname()
#print(host)
host = '192.168.1.13'
#host = 'fe80::a00:27ff:fef1:7361'
#host += '%enp0s3'
print(host)

port = 9999

#addrinfo = socket.getaddrinfo(host, port, socket.AF_INET6, socket.SOCK_STREAM, socket.SOL_TCP)
addrinfo = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM, socket.SOL_TCP)

print(addrinfo)

(family, socktype, proto, canonname, sockaddr) = addrinfo[0]

print ('Family ' , family)
print ('Socktype ', socktype)
print ('Proto ', proto)
print ('Canonname ', canonname)
print ('Sockaddr ', sockaddr)

# create a socket object
s = socket.socket(family, socktype, proto)
print(s)

# connection to hostname on the port.
s.connect(sockaddr)
#s.connect(('fe80::a00:27ff:fe38:46b0', 9999, 0, 0))

print(s)

# Receive no more than 1024 bytes
tm = s.recv(1024)

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))


