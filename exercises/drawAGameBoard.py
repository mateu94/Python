
def printHorizontalLines(board_size, box_size):
    for x in range(0,board_size):
        print(" ", end = "")
        for y in range(0,box_size):
            print("-", end = "")
    print("")

def printVerticalLinesAndValues(board_size, box_size, values, row):
    box_size = 3
    for x in range(0,board_size):
        print("|", end = "")
        for y in range(0,box_size):
            if y == box_size // 2:
                print(values[row,x], end = "")
            else:
                print(" ", end = "")
    print("|")

def printBoard(board_size, values):
    box_size = 3
    for x in range(0,board_size):
        printHorizontalLines(board_size, box_size)
        printVerticalLinesAndValues(board_size, box_size, values, x)
    printHorizontalLines(board_size, box_size)

if __name__ == "__main__":
    board_size = int(input("Enter the board size: "))
    positions_values = {(x,y): "-" for x in range(0, board_size) for y in range(0, board_size)}
    printBoard(board_size, positions_values)
