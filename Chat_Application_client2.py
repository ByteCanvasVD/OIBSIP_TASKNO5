import tkinter as tk
from tkinter import ttk
import socket
import threading

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat App")

        self.username = self.get_username()

        self.chat_history = tk.StringVar()
        self.message_var = tk.StringVar()

        # GUI elements
        self.chat_box = tk.Text(root, height=20, width=50, state=tk.DISABLED)
        self.message_entry = ttk.Entry(root, textvariable=self.message_var, width=40)
        self.send_button = ttk.Button(root, text="Send", command=self.send_message)

        # GUI layout
        self.chat_box.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.message_entry.grid(row=1, column=0, padx=10, pady=10)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        # Connect to the server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1", 12346))  # Updated port to 12346

        # Send the username to the server
        self.client_socket.send(self.username.encode("utf-8"))

        # Start a new thread to handle incoming messages
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

    def get_username(self):
        return input("Enter your username: ")

    def send_message(self):
        message = self.message_var.get()
        self.client_socket.send(message.encode("utf-8"))
        self.message_var.set("")

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    break

                message = data.decode("utf-8")
                self.update_chat_history(message)

            except socket.error:
                break

    def update_chat_history(self, message):
        self.chat_box.config(state=tk.NORMAL)
        self.chat_box.insert(tk.END, message + "\n")
        self.chat_box.config(state=tk.DISABLED)
        self.chat_box.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
