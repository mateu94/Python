import drawAGameBoard as board

usage_message = """
Enter the box position you want to mark (row,column).
Row and column coordinates must be between 1 and """

if __name__ == "__main__":
    board_size = int(input("Enter the board size: "))
    num_boxes = board_size * board_size
    occupied_boxes = 0
    positions_values = {(x,y): "-" for x in range(0, board_size) for y in range(0, board_size)}

    board.printBoard(board_size, positions_values)

    while occupied_boxes < num_boxes:
        usage = usage_message + str(board_size) + ": "
        position = input(usage)
        position = position.split(",")
        if positions_values[int(position[0])-1,int(position[1])-1] == "X":
            print("The box you have selected is already in use")
        else:
            positions_values[int(position[0])-1,int(position[1])-1] = "X"
            board.printBoard(board_size, positions_values)
            occupied_boxes += 1

