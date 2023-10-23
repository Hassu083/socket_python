import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect(('127.0.0.1',8000))


while True:
    message = input('Enter message: ').encode('utf-8')[:1024]
    client.send(message)
        
    response = client.recv(1024)
    response = response.decode("utf-8")

    if response.lower() == "closed":
            break

    print(f"Received: {response}")

# close client socket (connection to the server)
client.close()
print("Connection to server closed")