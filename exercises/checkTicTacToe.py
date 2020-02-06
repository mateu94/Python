import random

def checkHorizontal(game, board_size):
    for i in range(0, board_size):
        winner = [game[i][j] for j in range(0, board_size)]
        if winner.count(winner[0]) == board_size:
            return winner[0]
    return 0
     
def checkVertical(game, board_size):
    for i in range(0, board_size):
        winner = [game[j][i] for j in range(0, board_size)]
        if winner.count(winner[0]) == board_size:
            return winner[0]
    return 0
 
def checkDiagonal(game, board_size):
    diagonal1 = [x for x in range(0, board_size)]
    diagonal2 = [(x,y) for x in range(0, board_size) for y in range(0, board_size) if x + y == board_size - 1]
    winner = [game[x][x] for x in diagonal1]
    if winner.count(winner[0]) == board_size:
        return winner[0]
    winner = [game[x][y] for x,y in diagonal2]
    if winner.count(winner[0]) == board_size:
        return winner[0]
    return 0


def checkWinner(game, board_size):
    winner = checkHorizontal(game, board_size)
    if winner:
        return winner
    winner = checkVertical(game, board_size)
    if winner:
        return winner
    winner = checkDiagonal(game, board_size)
    if winner:
        return winner

if __name__ == "__main__":
    board_size = int(input("Enter the board size: "))
    game = []
    possibilities = [0, 1, 2]
    for x in range(0, board_size):
        game.append(random.choices(possibilities, k = board_size))
    for row in game:
        print(row)

    winner = checkWinner(game, board_size)
    if winner:
        print("The winner is player", winner)
    else: 
        print("It's a tie")

