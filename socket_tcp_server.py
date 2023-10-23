import socket

ip, port = '127.0.0.1', 8000

# creating tcp server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(0)


# accept incoming connections
client_socket, client_address = server.accept()
print(f"Accepted connection from {client_address[0]}:{client_address[1]}")


# receive data from the client
while True:
    request = client_socket.recv(1024)
    request = request.decode("utf-8") # convert bytes to string
    if request.lower() == "close":
        client_socket.send("closed".encode("utf-8"))
        break

    print(f"Received: {request}")

    client_socket.send('accepted'.encode('utf-8'))

client_socket.close()
print('Connection close')
server.close()