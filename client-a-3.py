# client.py
import socket

host = '132.70.227.105'
#host = socket.gethostname()  # Server IP
port = 444               # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("trying to connect to server")
s.connect((host, port))
print('Connection to %s established' % str(s.getsockname()))

# data received from sever
msgMAdataBA = s.recv(1024)
print(">>>", msgMAdataBA.decode('utf-8'))

while True:
    # User input
    dataAB = input(">>> ")
    msgAM = 'a' + dataAB
    s.sendall(msgAM.encode('utf-8'))
    s.close()

    while True:
        # Opening listening socket
        listening = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listening.bind((host, port))
        listening.listen(1)
        print("starting to listen for MB")
        conn, host = listening.accept()     # Client halts here until server initiates communication
        listening.close()   # Close listening socket
        msgMAdataBA = conn.recv(1024)
        print(">>>", msgMAdataBA.decode('utf-8'))
        continue

