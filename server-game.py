import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set up host and port
host = "127.0.0.1"
port = 8888

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(2)
print("Waiting for players...")

# Accept the first player's connection
player1, address1 = server_socket.accept()
print("Player 1 connected.")

# Send a message to player1 to indicate their player number
player1.send(b"You are player 1")

# Accept the second player's connection
player2, address2 = server_socket.accept()
print("Player 2 connected.")

# Send a message to player2 to indicate their player number
player2.send(b"You are player 2")

# Function to handle the game logic
def play_game(player1, player2):
    while True:
        # Receive the moves from both players
        move1 = player1.recv(1024).decode()
        move2 = player2.recv(1024).decode()

        # Determine the winner
        result = ""
        if move1 == move2:
            result = "It's a tie!"
        elif (move1 == "rock" and move2 == "scissors") or \
                (move1 == "paper" and move2 == "rock") or \
                (move1 == "scissors" and move2 == "paper"):
            result = "Player 1 wins!"
        else:
            result = "Player 2 wins!"

        # Send the result to both players
        player1.send(result.encode())
        player2.send(result.encode())

# Start the game
play_game(player1, player2)

# Close the connections
player1.close()
player2.close()
server_socket.close()
