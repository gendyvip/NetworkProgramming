from socket import *

s = socket (AF_INET, SOCK_STREAM)

host = "127.0.0.1"
port = 7000

s.connect((host, port))

while True:
    x = input("client : ")
    if (x == 'Q'):
        s.send(x.encode('utf=8'))
        break
    s.send(x.encode('utf=8'))
s.close()
