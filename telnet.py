from socket
import socket from telnetlib
import Telnet
import time
import re 
a = 0 
sock = socket() 
sock.connect(('ipadresi', 19001)) 
    print(sock.recv(256)) 
data = sock.recv(256) 
    print(data) 
last = data.decode().split("\n")[1] 
    print(last) lastt = last + '\n'
sock.send(lastt.encode()) a += 1
for i in range(1001): data = sock.recv(256) 
    print(data)
    last = data.decode() 
    lastt = re.sub("[^A-Za-z0-9 ' &]+", '', last) 
    lastt = lastt + '\n'
sock.send(lastt.encode()) 
a += 1 print(a) 
time.sleep(0.9)
