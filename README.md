# Server Client Project for Data Communcation class

# Project 1 Data Communication

Please run using command: python myclient.py/myserver.py LINK PORT TYPE index.html

# Server:
The server class first makes a server using blank host which results in localhost and a port number defined by user. It binds both the host and port and makes a server. 
Then I made a while loop which is an infinite loop for the server until “control-c” is pressed to close it.
While the loop is running it waits for requests. If request is received it is split by spaces and it detects what kind of request it is by comparing strings.
If it is a GET request it reads the index.html and sends back that file with 200OK command. If file is not found it sends a 404 message
If it is a PUT request then it reads the file sent and stores it on the server which is the local computer for this instance with 200OK command. If file is not found it sends a 404 message

<img src="https://github.com/ibrahimswati/Server-Client-Project-DataCommuncation/blob/main/servertest.png">


# PUT:
PUT class first creates and connects to socket and then sends a PUT request and then opens the file to put and reads it and then sends it as well and prints the data that has been sent and print the data received. 

<img src="https://github.com/ibrahimswati/Server-Client-Project-DataCommuncation/blob/main/PUT.png">

# GET:
GET class first creates and connects to socket and then sends a GET request. Then it waits for data to be received until it closes socket.

<img src="https://github.com/ibrahimswati/Server-Client-Project-DataCommuncation/blob/main/GET.png">
