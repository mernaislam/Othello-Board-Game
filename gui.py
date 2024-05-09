import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from game_manager import GameManager

class OthelloGUI:
    #constructor
    def __init__(self, boardSize = 8):
        self.gameManager = GameManager()
        self.boardSize = boardSize
        self.window = Tk()
        self.window.title("Welcome to Othello Game")
        self.hintBoard = []
        # define images used in the GUI
        self.greenImage = ImageTk.PhotoImage(Image.open("assets\\green.jpg").resize((90,90)))
        self.blackCoin = ImageTk.PhotoImage(Image.open("assets\\black_coin.png").resize((120,120)))
        self.whiteCoin = ImageTk.PhotoImage(Image.open("assets\\white_coin.png").resize((90,90)))
        self.hintCoin = ImageTk.PhotoImage(Image.open("assets\\hint_coin.png").resize((90,90)))
        self.create_board_buttons()

    def create_board_buttons(self):
        score1 = "Your Score: " + str(self.gameManager.board.players[0].score)
        score2 = "Computer Score: " + str(self.gameManager.board.players[1].score)
        coins1 = "Coins Left: " + str(self.gameManager.board.players[0].coins)
        coins2 = "Coins Left: " + str(self.gameManager.board.players[1].coins)
        self.score1 = Label(self.window, text=score1, font=('Arial', 17), bg="black", fg="white", width=29)
        self.score1.grid(row=0, column=2, columnspan=4)
        self.score2 = Label(self.window, text=score2, font=('Arial', 17), bg="black", fg="white", width=29)
        self.score2.grid(row=0, column=6, columnspan=4)
        self.coins1 = Label(self.window, text=coins1, font=('Arial', 17), bg="black", fg="white", width=29)
        self.coins1.grid(row=1, column=2, columnspan=4)
        self.coins2 = Label(self.window, text=coins2, font=('Arial', 17), bg="black", fg="white", width=29)
        self.coins2.grid(row=1, column=6, columnspan=4)

        self.buttons = [[tk.Button(self.window, image=self.greenImage, bg='#006822', width=90, height=90,
        command=lambda row=row, col=col: self.make_move(row, col)) for col in range(self.boardSize)] for row in range(self.boardSize)]
        
        for row in range(self.boardSize):
            for col in range(self.boardSize):
                self.buttons[row][col].grid(row=row+2, column=col+2)

    def make_move(self, row, col):
        #only update if the pressed button is a hint Coin and a valid move
        if self.buttons[row][col].cget("image") == str(self.hintCoin) and self.gameManager.board.update_board(row, col, 'b'): 
            self.buttons[row][col].configure(image=self.blackCoin) # change to black coin
            self.play_move()
        elif self.buttons[row][col].cget("image") == str(self.hintCoin):
            self.update_dashboard(1)
            self.hintBoard = self.gameManager.board.get_flip_moves('b')
            self.update_GUI_board(self.gameManager.board.board) 
        
    def play_move(self):
            if self.hintBoard != []:
                self.update_dashboard(0)
                self.update_GUI_board(self.gameManager.board.board)
            self.update_dashboard(1)
            self.hintBoard = self.gameManager.board.get_flip_moves('b')
            self.update_GUI_board(self.gameManager.board.board)
            if self.hintBoard == []:
                self.play_move()

    def update_dashboard(self, i):
        self.gameManager.board.update_score(self.gameManager.board.players)
        if i == 0:
            self.gameManager.board.players[i].make_move()
            # self.gameManager.board.board[move[0][0]][move[0][1]] = 'w'
        else:
            self.gameManager.board.players[i].make_move(self.gameManager.board)
        score1 = "Your Score: " + str(self.gameManager.board.players[0].score)
        score2 = "Computer Score: " + str(self.gameManager.board.players[1].score)
        coins1 = "Coins Left: " + str(self.gameManager.board.players[0].coins)
        coins2 = "Coins Left: " + str(self.gameManager.board.players[1].coins)
        self.score1.config(text=score1)
        self.coins1.config(text=coins1)
        self.score2.config(text=score2)
        self.coins2.config(text=coins2)

    def update_GUI_board(self, board):
        for row in range(8):
            for col in range(8):
                if board[row][col] == 'w':
                    self.buttons[row][col].configure(image=self.whiteCoin)
                elif board[row][col] == 'b':
                    self.buttons[row][col].configure(image=self.blackCoin)
                else:
                    self.buttons[row][col].configure(image=self.greenImage)

        for x,y in self.hintBoard:
            self.buttons[x][y].configure(image=self.hintCoin)


    def __del__(self):
        self.window.mainloop()

    def run(self):
        self.hintBoard = self.gameManager.board.get_flip_moves('b')
        self.update_GUI_board(self.gameManager.board.board)
        self.__del__()

# app starts here
game = OthelloGUI()
game.run()