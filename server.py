# echo_server.py
import socket

flag = 0
a_ip = '172.18.34.37'
b_ip = '172.18.34.37'
port = 444


def connect():
    global flag      # Indicates if this is the first connection (A)
    global a_ip      # A's IP address
    global b_ip
    global port

    if flag == 0:
        host = ''        # Symbolic name meaning all available interfaces
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        s.close()
        conn.sendall('Chat initiated!'.encode('utf-8'))
        flag = 2
        return conn

    elif flag == 1:    # This means its the first connection - A
        a_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a_conn.connect((a_ip, port))
        #print("first connection from A established by", addr[0])
        #a_ip = addr[0]
        flag = 2
        return a_conn

    elif flag == 2:    # This means its the second connection - B
        b_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        b_conn.connect((b_ip, port))
        #print("second connection from B established by", addr[0])
        #b_ip = addr[0]
        flag = 1
        return b_conn


conn = connect()

while True:
    message = conn.recv(1024).decode()
    if not message:
        break

    print("data received is %s" % str(message))

    if message[0] == 'a':
        print('message contains data from A to B')
        msgAMdataAB = message[1:]
        conn.close()
        print('connection to A is closed')
        print('attempting to connect to B')
        port = 555
        conn = connect()
        print('connection to B is established')
        conn.sendall(msgAMdataAB.encode('utf-8'))

    if message[0] == 'b':
        print('message contains data from B to A')
        msgBMdataBA = message[1:]
        conn.close()
        print('connection to B is closed')
        print('attempting to connect to A')
        port = 444
        conn = connect()
        print('connection to A is established')
        conn.sendall(msgBMdataBA.encode('utf-8'))
