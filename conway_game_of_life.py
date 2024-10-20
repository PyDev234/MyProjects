# Program: Conway's Game of Life
import copy
import random
import time

size = 25
board = []
b = []

def print_board() -> None:
    for row in board:
        for col in row: print('\033[41m#' if col else '\033[44m ', end="")
        print(end="\033[0m\n")
    print("\033[{}A\033[{}D".format(size + 1, size))

def set_board() -> None:
    global board
    for row in range(size):
        cols = random.randint(1, size)
        cols = [1 for col in range(cols)] + [0 for col in range(size-cols)]
        random.shuffle(cols)
        board.append(cols)
    
    # printing the board
    print_board()

def find_alive_neighbours(row: int = 0, col: int = 0) -> int:
    n = 0
    for y in range(-1, 2):
        for x in range(-1, 2):
            if ((-1<(y+row)<size) and (-1<(x+col)<size) and b[row+y][col+x]) and (y!=0 or x!=0): n += 1
    return n

def main():
    global board, b
    
    # set the initial configuration of board
    set_board()

    # copying the configuration of board into 'b'. And start the time counter
    b = copy.copy(board)
    t = time.perf_counter()

    # Hiding the cursor
    print(end="\033[?25l")

    # Continue to print the board generation after generation until KeyboardInterrupt is Pressed (i.e. CTRL + C)
    try:
        # 'i' for counting the no. of generations passed.
        for i in range(100000000):
            # setting the next value of each block in current generation using duplicated data from 'b'.
            for row in range(size):
                for col in range(size):
                    # finding the no. of alive neighbours.
                    n = find_alive_neighbours(row, col)
                    # if 'n' is 3 then it will be alive no matter what and if 'n' is 2 then will be alive if it is previously alive.
                    board[row][col] = int(n==3 or (n==2 and b[row][col]))
            # Print the current generation
            print_board()
            # duplicate the changed generation to 'b'.
            b = copy.copy(board)
            # time.sleep(0.5)
    except KeyboardInterrupt as e:
        # make the cursor visible again and reset color of terminal
        print(end="\033[0m\033[?25h")
        # prints the no. of generation currently printed
        gens = i//int(time.perf_counter() - t)
        print("Gens:", gens)

if __name__ == '__main__':
    main()