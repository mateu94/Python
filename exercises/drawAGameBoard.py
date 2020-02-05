
def printHorizontalLines(board_size, box_size):
    for x in range(0,board_size):
        print(" ", end = "")
        for y in range(0,box_size):
            print("-", end = "")
    print("")

def printVerticalLines(board_size, box_size):
    box_size = 3
    for x in range(0,board_size):
        print("|", end = "")
        for y in range(0,box_size):
            print(" ", end = "")
    print("|")

def printBoard(board_size):
    box_size = 3
    for x in range(0,board_size):
        printHorizontalLines(board_size, box_size)
        printVerticalLines(board_size, box_size)
    printHorizontalLines(board_size, box_size)

if __name__ == "__main__":
    board_size = int(input("Enter the board size: "))
    printBoard(board_size)
