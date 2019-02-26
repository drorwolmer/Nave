import socket
import sys
from _dummy_thread import *

host = ''
port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(1)
print('wait for a connection')
def threaded_client(conn):
    conn.send(str.encode('welcome \n'))

    while True:
        data = conn.recv(4096)
        data = (str(data)).upper()
        reply = " --> "+str(data)
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()

while True:
    conn, addr =s.accept()
    print('connected to: '+addr[0]+':'+str(addr[1]))

    start_new_thread(threaded_client(conn,))