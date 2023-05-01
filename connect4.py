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
    
    active_player = 1
    players = ["First","Second"]
    symbols = ["X", "O"]
    intro()
    print_board(board)
    while not endgame():
        active_player = abs(active_player -1)
        choice = validate_choice(players,active_player)
        



def check_placement(col, board,symbols, active_player):
    for i in range(5,-1,-1):
        if board[i][col-1] == None:
            return True
    print("Column full, try another column")
    return False
        
    


def validate_choice(players, active_player):
    valid = False
    while not valid:
        col = input(f"{players[active_player]} player, it's your turn. Choose a column: ")
        try:
           col = int(col) 
        except:
            print("Please enter a number between 1 and 7")
            continue
        if col<1 or col>7:
            print("Please enter a number between 1 and 7")
            continue
        valid = True
    
    return col
        

    



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
   


def endgame():
    return False
    

    


if __name__ == "__main__":
    main()


