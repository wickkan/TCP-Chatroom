"""
Code inspired by FreeCodeCamp: youtube.com/watch?v=FGdiSJakIS4&ab_channel=freeCodeCamp.org
"""

import threading
import socket

host = '127.0.0.1'  # localhost

port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
names = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.receive(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = names[index]
            broadcast(f'{nickname} left the chat.'.encode('ascii'))
            names.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
