import socket
import threading

name = input("Choose a name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NAME':
                client.send(name.encode('ascii'))
                pass
            else:
                print(message)
        except:
            print('An error occurred.')
            client.close()
            break


def write():
    while True:
        msg = f'{name}: {input("")}'
        client.send(msg.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
