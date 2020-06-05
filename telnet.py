import socket


target_host = "34.248.251.3"
target_port = 19001

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((target_host, target_port))


for x in range(1001):
    response = s.send(s)
    response = s.recv(4096)
    print(response)










