
from player import Player
from board import Board


class Game:

    def __init__(self):
        print("Start spel")
        name_x = input("Please input the name of player 1 who will play with the token X: ")
        p1 = Player(name_x, "X")
        name_y = input("Please input the name of player 2 who will play with the token Y: ")
        p2 = Player(name_y, "O")

        print(p1)
        print(p2)

        won = False
        board = Board(7, 6)
        board.print_board()
        
        while not won:
            selection = input(f"Please select the number of column you want to drop a token: ")
            if not selection.isnumeric():
                print("Wrong you dickhead!!! Please give me a fucking number!!!")
                continue

            column = int(selection) - 1
            if board.is_valid_column(column):
                print("That column doenst exist you little shit. Give me a valid one!!")
                continue

        

        row = board.empty_row_for_column(0)
        board.add_token(row, 0, "X")
        board.print_board()

game = Game()