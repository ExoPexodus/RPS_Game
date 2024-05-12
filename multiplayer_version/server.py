import socket

def handle_client(client_socket, client_number):
    while True:
        try:
            user_choice = client_socket.recv(1024).decode().lower().strip()
            if not user_choice:
                break
            print(f"Player {client_number} chose: {user_choice}")
            client_socket.send("Waiting for the other player...".encode())
            if user_choice != "":
                client_socket.send("Waiting for the other player...".encode())
                other_choice = client_socket.recv(1024).decode().lower().strip()
                print(f"Player {client_number} chose: {other_choice}")
                if other_choice != "":
                    determine_winner(user_choice, other_choice, client_socket)
                    break
        except Exception as e:
            print(f"Error: {e}")
            break
    client_socket.close()

def determine_winner(player1_choice, player2_choice, client_socket):
    if player1_choice == player2_choice:
        client_socket.send("It's a tie!".encode())
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
         (player1_choice == 'paper' and player2_choice == 'rock') or \
         (player1_choice == 'scissors' and player2_choice == 'paper'):
        client_socket.send("Player 1 wins!".encode())
    else:
        client_socket.send("Player 2 wins!".encode())

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5555))
    server_socket.listen(2)
    print("Waiting for players to join...")

    client_number = 1
    while True:
        client_socket, address = server_socket.accept()
        print(f"Player {client_number} connected from {address}")
        client_socket.send("Welcome to Rock-Paper-Scissors! Please wait for the other player to connect.".encode())
        client_socket.send(f"You are Player {client_number}".encode())
        client_socket.send("Enter your choice (rock, paper, or scissors): ".encode())
        client_socket.send("".encode())
        handle_client(client_socket, client_number)
        client_number += 1
        if client_number > 2:
            break

    server_socket.close()

if __name__ == "__main__":
    start_server()
