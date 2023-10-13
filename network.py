import socket

HOST = socket.gethostname()
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    while True:
        message = input("Write your message: ")
        client_socket.sendall(message.encode())

        data = client_socket.recv(1024)
        print('Received', repr(data.decode()))

        if message.lower() == "exit":
            break

