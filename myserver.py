import socket
import sys

BUFFER_SIZE = 1024
host = ''

def server(host, port): #Define server
    asgn1_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket object
    asgn1_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    asgn1_socket.bind((host, port)) #Bind Socket
    asgn1_socket.listen(5) #Accept only 5 devices
    while True: #Infinite Loop for server
        client_socket, address = asgn1_socket.accept()
        print("Connection from: " + str(address))
        req = client_socket.recv(1024) #Get request 1kb only
        print(req)
        req = req.decode().split(" ") #Split request so if loop can be used to check

        if req[0]=="GET": #If method GET is called
            if req[1] == "/index.html": #Check if index file is requested
                try: #Loop to see if index file is present
                    f = open("index.html", 'r') #Open index and read
                    for indx in f.readlines():
                        print(repr(indx))
                        client_socket.sendall(str.encode(indx)) #Send index file to client
                        indx = f.read(1024)
                        f.close()
                        client_socket.sendall(str.encode("HTTP/1.0 200 OK")) #Send 200 OK
                except IOError: #Error if index file not present
                    client_socket.sendall(str.encode("404 file not found"))
                    print("404 file not found")
                    client_socket.close()

            else: #Error if file other than index is requested
                client_socket.sendall(str.encode("404 not found"))
                print("404 not found")
                client_socket.close()

        if req[0]=="PUT": #If method PUT is called
            if req[1]=="/test.txt": #Check if test.txt is requested
                with open('test.txt', 'wb') as f:
                    data = client_socket.recv(BUFFER_SIZE).decode()
                    print(data)
                    f.write(data)
                f.close()
                client_socket.sendall(str.encode("200 OK File Created"))
                client_socket.close()

            else: #If test.txt is not requested
                client_socket.sendall(str.encode("404 not found"))
                print("404 not found")
                client_socket.close()



def main(): #Main
    port = int(sys.argv[1]) #Input port number
    print('Server started on port: {}\nPlease press control-c to exit.\n'.format(port))
    server(host, port)

if __name__ == "__main__":
    main()
