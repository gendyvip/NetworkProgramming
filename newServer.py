from socket import *                            
from _thread import *                          


host = '127.0.0.1'                              
port = 12221                                     
clients = []

sock = socket((AF_INET), SOCK_STREAM)           
sock.bind((host, port))                          
sock.listen(20)                                 
print("server is running...")
print("server ip is " + host)
print("server port is "+ str(port))

                                               
def recieving(conn , addr):
    while True:
        msg = str(addr[1]) + "-> " + conn.recv(2048).decode()
        
        for client in clients:
            if client != conn:
                client.send(msg.encode())

while True:
    conn, addr = sock.accept()
    print(str(addr[1]) + " joined the room " )
    msg = "connection from "+ str(addr[1]) + " established \n"
    for client in clients:
            client.send(msg.encode())
    clients.append(conn)
    start_new_thread(recieving, (conn, addr))
    



