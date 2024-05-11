import socket

def start_server():
    host = "192.168.56.1"
    port = 9999

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(data)

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
