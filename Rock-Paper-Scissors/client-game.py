import socket
import tkinter as tk
from tkinter import messagebox

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set up host and port
host = "127.0.0.1"
port = 8888

# Connect to the server
client_socket.connect((host, port))

# Receive the player number from the server
player_number = client_socket.recv(1024).decode()

# Create a Tkinter window
window = tk.Tk()
window.title(f"Rock Paper Scissors - {player_number}")
window.geometry("300x250")

# Function to handle button clicks
def send_move(move):
    client_socket.send(move.encode())
    result = client_socket.recv(1024).decode()
    messagebox.showinfo("Result", result)

# Create buttons for moves with unique colors
rock_btn = tk.Button(window, text="Rock", width=20, command=lambda: send_move("rock"), bg="gray")
paper_btn = tk.Button(window, text="Paper", width=20, command=lambda: send_move("paper"), bg="light blue")
scissors_btn = tk.Button(window, text="Scissors", width=20, command=lambda: send_move("scissors"), bg="pink")

# Add buttons to the window
rock_btn.pack(pady=10)
paper_btn.pack(pady=10)
scissors_btn.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()

# Close the connection
client_socket.close()
