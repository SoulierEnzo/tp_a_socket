import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("172.16.21.49",63000))
while True:
    client.send(input().encode())
