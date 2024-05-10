import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from time import sleep
class OthelloGUI:
    #constructor
    def __init__(self, gm, boardSize = 8):
        self.boardSize = boardSize
        self.window = Tk()
        self.window.title("Welcome to Othello Game")
        self.hintBoard = []
        self.gm = gm
        # define images used in the GUI
        self.greenImage = ImageTk.PhotoImage(Image.open("assets\\green.jpg").resize((90,90)))
        self.blackCoin = ImageTk.PhotoImage(Image.open("assets\\black_coin.png").resize((120,120)))
        self.whiteCoin = ImageTk.PhotoImage(Image.open("assets\\white_coin.png").resize((90,90)))
        self.hintCoin = ImageTk.PhotoImage(Image.open("assets\\hint_coin.png").resize((90,90)))
        self.create_board_buttons()

    def create_board_buttons(self):
        score1 = "Your Score: " + str(2)
        score2 = "Computer Score: " + str(2)
        coins1 = "Coins Left: " + str(30)
        coins2 = "Coins Left: " + str(30)
        self.score1 = Label(self.window, text=score1, font=('Arial', 17), bg="black", fg="white", width=29)
        self.score1.grid(row=0, column=2, columnspan=4)
        self.score2 = Label(self.window, text=score2, font=('Arial', 17), bg="black", fg="white", width=29)
        self.score2.grid(row=0, column=6, columnspan=4)
        self.coins1 = Label(self.window, text=coins1, font=('Arial', 17), bg="black", fg="white", width=29)
        self.coins1.grid(row=1, column=2, columnspan=4)
        self.coins2 = Label(self.window, text=coins2, font=('Arial', 17), bg="black", fg="white", width=29)
        self.coins2.grid(row=1, column=6, columnspan=4)

        self.buttons = [[tk.Button(self.window, image=self.greenImage, bg='#006822', width=90, height=90, command=lambda row=row, col=col: self.make_move(row, col)) for col in range(self.boardSize)] for row in range(self.boardSize)]
        
        for row in range(self.boardSize):
            for col in range(self.boardSize):
                self.buttons[row][col].grid(row=row+2, column=col+2)

    def make_move(self, row, col):
        self.gm.main(row, col)

    def update_dashboard(self, score1, score2, coins1, coins2):
        score1 = "Your Score: " + str(score1)
        score2 = "Computer Score: " + str(score2)
        coins1 = "Coins Left: " + str(coins1)
        coins2 = "Coins Left: " + str(coins2)
        self.score1.config(text=score1)
        self.coins1.config(text=coins1)
        self.score2.config(text=score2)
        self.coins2.config(text=coins2)

    def update_GUI_board(self, board, hint_board):
        for row in range(8):
            for col in range(8):
                if board[row][col] == 'w':
                    self.buttons[row][col].configure(image=self.whiteCoin)
                elif board[row][col] == 'b':
                    self.buttons[row][col].configure(image=self.blackCoin)
                else:
                    self.buttons[row][col].configure(image=self.greenImage)

        for x,y in hint_board:
            self.buttons[x][y].configure(image=self.hintCoin)

    def show_winner(self, msg):
        self.winner = Label(self.window, text=msg, font=('Arial', 30), bg="black", fg="white", width=29)
        self.winner.grid(row=5, column=2, columnspan=8)

    def __del__(self):
        self.window.mainloop()