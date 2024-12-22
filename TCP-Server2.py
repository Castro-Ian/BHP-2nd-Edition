import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        # Accept a client connection
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')

        # Create a thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        # Receive data from the client
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')

        # Send acknowledgment to the client
        sock.send(b'ACK')

if __name__ == '__main__':
    main()
