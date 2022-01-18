import socket
import sys

BUFFER_SIZE = 1024

def GET(host, port, name):
    asgn1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create Socket
    asgn1_socket.connect((host, port)) #Connect to socket
    sendreq = 'GET /{} HTTP/1.1\r\nHost:{} \r\n\r\n'.format(name, host) #Request
    asgn1_socket.send(sendreq.encode()) #Send request
    rcvddata = asgn1_socket.recv(1024) #Recieve data
    print(repr(rcvddata)) #Print data

def PUT(host, port, name):
    asgn1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create Socket
    asgn1_socket.connect((host, port)) #Connect to socket
    sendreq = 'PUT /{} HTTP/1.1\r\nHost:{} \r\n\r\n'.format(name, host) #Request
    asgn1_socket.send(sendreq.encode()) #Send request
    file = name
    with open(file, 'r') as f: #Open file and read
            for txt in f.readlines():
                asgn1_socket.send(txt.encode()) #Send file
    rcvddata = asgn1_socket.recv(1024) #Recieve data
    print(rcvddata) #Print data
    asgn1_socket.close() #Close socket
    print('Data sent is: {}'.format(txt))


def main():

    host = sys.argv[1]
    port = int(sys.argv[2])
    method = sys.argv[3]
    name = sys.argv[4]

    if method == 'GET':
        print('Starting GET on host: {}, port: {}'.format(host, port))
        GET(host, port, name)

    if method == 'PUT':
        print('Starting PUT on host: {}, port: {}'.format(host, port))
        PUT(host, port, name)


if __name__ == "__main__":
    main()
