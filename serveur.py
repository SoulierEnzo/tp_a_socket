import socket

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(("172.16.21.49",63000))
serveur.listen(1)
conn, addr = serveur.accept()
message = conn.recv(1024).decode()

print(message)

