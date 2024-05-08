import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from game_manager import GameManager

class OthelloGUI:
    def __init__(self, boardSize = 8):
        self.gameManager = GameManager()
        self.boardSize = boardSize
        self.window = Tk()
        self.xMove = 0
        self.yMove = 0
        self.window.title("Welcome to Othello Game")
        self.board = [[' ' for _ in range(self.boardSize)] for _ in range(self.boardSize)]
        self.greenImage = ImageTk.PhotoImage(Image.open("assets\\green.jpg").resize((90,90)))
        self.blackCoin = ImageTk.PhotoImage(Image.open("assets\\black_coin.png").resize((120,120)))
        self.whiteCoin = ImageTk.PhotoImage(Image.open("assets\\white_coin.png").resize((90,90)))
        self.hintCoin = ImageTk.PhotoImage(Image.open("assets\\hint_coin.png").resize((90,90)))
        self.create_board_buttons()

    def get_x_move(self):
        return self.xMove

    def create_board_buttons(self):
        self.buttons = [[tk.Button(self.window, image=self.greenImage, font=('Arial', 24), bg= 'green', width=90, height=90, compound=tk.CENTER,
    command=lambda row=row, col=col: self.make_move(row, col)) for col in range(self.boardSize)] for row in range(self.boardSize)]
        
        for row in range(self.boardSize):
            for col in range(self.boardSize):
                self.buttons[row][col].grid(row=row, column=col)

        self.buttons[3][3].config(image=self.whiteCoin)
        self.buttons[3][4].config(image=self.blackCoin)
        self.buttons[4][4].config(image=self.whiteCoin)
        self.buttons[4][3].config(image=self.blackCoin)

    def make_move(self, row, col):
        if(self.buttons[row][col].cget("image") == str(self.hintCoin)):
            print('auhaagaaa')
            self.buttons[row][col].configure(image=self.blackCoin)

        print('yahaaa')
        self.xMove = row
        self.yMove = col
        self.gameManager.board.update_board(row, col)
        self.update_board(self.gameManager.board.board, 8)
        self.gameManager.board.display_valid_moves()
        self.update_board(self.gameManager.board.board, 8)



    def update_board(self, board, sz):
        for row in range(sz):
            for col in range(sz):
                if board[row][col] == 'h':
                    self.buttons[row][col].configure(image=self.hintCoin)
                elif board[row][col] == 'w':
                    self.buttons[row][col].configure(image=self.whiteCoin)
                elif board[row][col] == 'b':
                    self.buttons[row][col].configure(image=self.blackCoin)

    def __del__(self):
        self.window.mainloop()

    def run(self):
        self.gameManager.board.display_valid_moves()
        self.update_board(self.gameManager.board.board, 8)
        self.window.mainloop()

game = OthelloGUI()
game.run()