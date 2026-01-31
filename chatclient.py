import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'   
port = 12345
client_socket.connect((host, port))
print("Connected to server.")

while True:
    msg = input("Client: ")
    client_socket.send(msg.encode())

    if msg.lower() == "exit":
        break

    server_reply = client_socket.recv(1024).decode()
    print("Server:", server_reply)

client_socket.close()