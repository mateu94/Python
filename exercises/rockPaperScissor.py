choices = ["rock", "paper", "scissors"]

while True:
    player1_choice = input("Player 1, enter your choice: ")
    while player1_choice not in choices:
        player1_choice = input("Please, enter a valid choice [rock, paper, scissors]: ")
    player2_choice = input("Player 2, enter your choice: ")
    while player2_choice not in choices:
        player2_choice = input("Please, enter a valid choice [rock, paper, scissors]: ")
        
    if player1_choice == player2_choice:
        print("It's a tie")
    elif player1_choice == "rock": 
        if player2_choice == "paper":
            print("Player 2 wins")
        else:
            print("Player 1 wins")
    elif player1_choice == "paper": 
        if player2_choice == "scissors":
            print("Player 2 wins")
        else: 
            print("Player 1 wins")
    elif player1_choice == "scissors": 
        if player2_choice == "rock":
            print("Player 2 wins")
        else: 
            print("Player 1 wins")

    next_game = input("Do you wanna play another time?[y/n]: ")
    if next_game == "n":
        break
