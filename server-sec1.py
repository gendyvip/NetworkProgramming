from socket import *

#AF_INET, AF_UNIX >> IPV4 ,SOCK_STREAM >> TCP, SOCK_DGRAM >> UDP
s = socket (AF_INET, SOCK_STREAM)  

host = "127.0.0.1"
port = 7000

#BIND THE PORT TO THE HOSTNAME
s.bind((host, port))

#LISTENING TO THE INCOMING REQUESTS (NUMBER OF INCOMING REQUESTS)
s.listen(5)

#ACCEPT CONNECTION FROM THE CLIENT
c,ad = s.accept()
print("Connection From ",ad[0])

while True:
    x = c.recv(2048)
    print("client :", x.decode('utf=8'))
    if (x.decode('utf=8') == 'Q'):
        break    
s.close()
