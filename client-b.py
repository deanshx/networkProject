# client.py
import socket

host = ''
#host = socket.gethostname()  # Servers IP needs to be here
port = 555                   # The same port as used by the server

# Opening listening socket
listening = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listening.bind((host, port))
listening.listen(1)
print("Opened listening socket - start listening for server M")
conn, addr = listening.accept()

print('Connection to %s established' % str(conn.getsockname()))

# data received from sever
msgMBdataAB = conn.recv(1024)
print(">>>", msgMBdataAB.decode('utf-8'))

while True:
    # User input
    dataBA = input(">>> ")
    msgBM = 'b' + dataBA
    conn.sendall(msgBM.encode('utf-8'))
    conn.close()

    while True:
        # Opening listening socket
        listening = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listening.bind((host, port))
        listening.listen(1)
        print("starting to listen for MA")
        conn, addr = listening.accept()
        listening.close()   # Close listening socket
        msgMAdataBA = conn.recv(1024)
        print(">>>", msgMAdataBA.decode('utf-8'))
        continue
