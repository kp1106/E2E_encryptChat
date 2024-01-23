import socket
import threading

import rsa


choice = input("Do you want to host (1) or to connect (2): ")

if choice == "1":
    server = socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.0.210", 9999))
    server.listen()

    client, _= server.accept()
elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.0.210", 9999))
else:
    exit()

def  sending_messages(c):
    while True:
        message = input("")
        c.send(message.encode())
        print("You: " + message)

def  recieving_messages(c):
    while True:
        message = input("")
        print("Partner: " + c.recv(1024).decode())


threading.Thread(target=sending_messages, args=(client)).start()
threading.Thread(target=sending_messages, args=(client)).start()