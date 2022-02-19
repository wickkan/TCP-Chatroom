"""
Code inspired by FreeCodeCamp: youtube.com/watch?v=FGdiSJakIS4&ab_channel=freeCodeCamp.org
"""

import threading
import socket

host = '127.0.0.1'  # localhost
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

clients = []
names = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = names[index]
            broadcast('{} left the chat.'.format(nickname).encode('ascii'))
            names.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        client.send('NAME'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        names.append(nickname)
        clients.append(client)

        print('Name of the client is {}'.format(nickname))
        broadcast('{} joined the chatroom!'.format(nickname).encode('ascii'))
        client.send('Connected to the server.'.encode(ascii))

        thread = threading.Thread(target=handle, args=(client))
        thread.start()


print("Server is ready...")
receive()
