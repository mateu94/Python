import random

player_symbol = {"-": 0, "X": 1, "O": 2}

def checkHorizontal(game, board_size):
    no_more_moves = 0
    for i in range(0, board_size):
        winner = [game[i,j] for j in range(0, board_size) if game[i,j] is not "-"]
        if len(winner) and winner.count(winner[0]) == board_size:
            return player_symbol[winner[0]]
        elif "X" in winner or "O" in winner:
            no_more_moves = 3
    return no_more_moves
     
def checkVertical(game, board_size):
    for i in range(0, board_size):
        winner = [game[j,i] for j in range(0, board_size) if game[j,i] is not "-"]
        if len(winner) and winner.count(winner[0]) == board_size:
            return player_symbol[winner[0]]
    return 0
 
def checkDiagonal(game, board_size):
    diagonal1 = [x for x in range(0, board_size)]
    diagonal2 = [(x,y) for x in range(0, board_size) for y in range(0, board_size) if x + y == board_size - 1]
    winner = [game[x,x] for x in diagonal1 if game[x,x] is not "-"]
    if len(winner) and winner.count(winner[0]) == board_size:
        return player_symbol[winner[0]]
    winner = [game[x,y] for x,y in diagonal2 if game[x,y] is not "-"]
    if len(winner) and winner.count(winner[0]) == board_size:
        return player_symbol[winner[0]]
    return 0


def checkWinner(game, board_size):
    winner = checkHorizontal(game, board_size)
    if winner == 1 or winner == 2:
        return winner
    winner = checkVertical(game, board_size)
    if winner:
        return winner
    winner = checkDiagonal(game, board_size)
    if winner:
        return winner
    return 0

if __name__ == "__main__":
    board_size = int(input("Enter the board size: "))
    game = {(x,y): "-" for x in range(0, board_size) for y in range(0, board_size)}
    possibilities = [0, 1, 2]
    for x in game:
        game[x] = random.choice(possibilities)
    for row in game:
        print(row, ": ", game[row], sep = "")

    winner = checkWinner(game, board_size)
    if winner:
        print("The winner is player", winner)
    else: 
        print("It's a tie")
