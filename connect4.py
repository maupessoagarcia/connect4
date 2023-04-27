#intro
#create empty board - OK
#select players
#select placement
#check where piece will fall
#check if 4 are connected - winner
#announce winner
import os

def main():
    os.system("cls")
    board = [[None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None],
             ]
    
    active_player = 0
    players = ["First","Second"]
    symbols = ["X", "O"]
    intro()
    print_board(board)


    


def print_board(board):
    print()
    print("  1   2   3   4   5   6   7")
    print()
    for row in board:
        print("| ", end="")
        for cell in row:
            print(cell if cell is not None else "_", end = " | ")
        print()
    print()


def placement(board):
    pass

def intro():
    print("------------------------")
    print("Welcome to Connect4 Game")
    print("------------------------")
   



if __name__ == "__main__":
    main()