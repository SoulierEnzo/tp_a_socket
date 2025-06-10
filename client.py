import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("172.16.21.49",63000))
client.send("hello la team !".encode())
client.send("Ceci est un message !".encode())
client.send("Olala c'est la décadence !".encode())
