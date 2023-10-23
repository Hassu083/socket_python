import socket


ip, port = '127.0.0.1', 8000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((ip, port))

while True:
    client_Address = server.recvfrom(1024)
    if client_Address[0].decode("utf-8") == 'closed':
        server.sendto('Bye, client'.encode('utf-8'),client_Address[1])
        break
    print(f'Message form {client_Address[1]} is, {client_Address[0]}')
    server.sendto('Hello, client'.encode('utf-8'),client_Address[1])

server.close()


