import socket
import json
import keyboard

online_users = {}

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_ip = "10.81.40.15"
server_port = 5555
server_socket.bind((server_ip,server_port))
server_socket.listen(5)
print(f'listening on port {server_port}')

while True:
    client_socket,client_ad = server_socket.accept()
    print(f'connection accepted with {client_ad}')
    username = client_socket.recv(1024).decode('utf-8')
    online_users[username] = client_ad
    users_json = json.dumps(online_users)
    client_socket.send(users_json.encode('utf-8'))
    client_socket.close()

