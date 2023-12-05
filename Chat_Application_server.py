import socket
import threading

# Dictionary to store user information (username, socket)
users = {}

def handle_client(client_socket, username):
    # Broadcast a new user joined message
    broadcast(f"{username} joined the chat.")

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break

            message = data.decode("utf-8")
            broadcast(f"{username}: {message}")

        except socket.error:
            break

    # Remove the user and broadcast their departure
    del users[username]
    broadcast(f"{username} left the chat.")

def broadcast(message):
    for user_socket in users.values():
        try:
            user_socket.send(message.encode("utf-8"))
        except socket.error:
            pass

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12346))  # Updated port to 12346
    server_socket.listen(5)

    print("Server listening on port 12346...")  # Updated port in print statement

    while True:
        client_socket, client_address = server_socket.accept()

        # Receive username from the client
        username = client_socket.recv(1024).decode("utf-8")

        # Add the user to the dictionary
        users[username] = client_socket

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
        client_thread.start()

if __name__ == "__main__":
    start_server()

