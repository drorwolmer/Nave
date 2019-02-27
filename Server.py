import socket
import sys
# we never want to `import *`
from _dummy_thread import *

# what does `host` mean?
host = ''
# Let's have the port as a command line argument
port = 10000


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    # checkout logging module
    # logging.exception("Could not bind")
    print(str(e))
    # Also, this is a good place to exit, no? the next call will fail

# we dont need to define the `backlog` parameter here, s.listen() is enough
s.listen(1)
# better to use logging module, not print
# logging.info("Waiting for a connection")
print('wait for a connection')
def threaded_client(conn):
    conn.send(str.encode('welcome \n'))

    while True:
        data = conn.recv(4096)
        data = (str(data)).upper()
        reply = " --> "+str(data)
        # You want to check for this right after the recv(), not here
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()

while True:
    conn, addr =s.accept()
    # use logging
    print('connected to: '+addr[0]+':'+str(addr[1]))
    # You are not actually starting a new thread here, you are executing this in the main thread
    start_new_thread(threaded_client(conn,))
