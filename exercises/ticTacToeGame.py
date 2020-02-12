import random
import ticTacToeDraw as tttDraw
import drawAGameBoard as board
import checkTicTacToe as cttt

def IANewBox(board_size, positions_values):
    x_position = random.choice(range(0, board_size))
    y_position = random.choice(range(0, board_size))
    while positions_values[x_position, y_position] is not "-":
        x_position = random.choice(range(0, board_size))
        y_position = random.choice(range(0, board_size))
    print("The opponent movement is [", x_position+1, ", ", y_position+1, "]", sep = "")
    positions_values[x_position, y_position] = "O"


if __name__ == "__main__":
    print("Welcome to the Tic Tac Toe game")
    board_size = int(input("Enter the board size: "))
    num_boxes = board_size * board_size
    occupied_boxes = 0
    positions_values = {(x,y): "-" for x in range(0, board_size) for y in range(0, board_size)}
    board.printBoard(board_size, positions_values)

    while occupied_boxes < num_boxes:
        occupied_boxes = tttDraw.drawNewBox(board_size, positions_values, occupied_boxes)
        if cttt.checkWinner(positions_values, board_size):
            print("You have won")
            break
        if occupied_boxes < num_boxes:
            IANewBox(board_size, positions_values)
            board.printBoard(board_size, positions_values)
            occupied_boxes += 1
            winner = cttt.checkWinner(positions_values, board_size)
            if winner == 2:
                print("YOU DIED")
                break

