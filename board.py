from computer_player import ComputerPlayer
from player import Player

class Board:
    def __init__(self):
        self.n = 8
        self.board = [[' ' for _ in range(self.n)] for _ in range(self.n)]
        self.board[3][3] = 'w'
        self.board[3][4] = 'b'
        self.board[4][4] = 'w'
        self.board[4][3] = 'b'
        self.players = [Player(), ComputerPlayer()]

    def update_board(self, x, y, c):
        lst = self.valid_move(x,y,c)
        if lst != []:
            self.flip(lst, c)
            self.board[x][y] = c
            return True
        return False

    def update_score(self, players):
         players[0].score = 0
         players[1].score = 0
         for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col] == 'w':
                    players[1].score += 1
                elif self.board[row][col] == 'b':
                    players[0].score += 1

    def get_legal_moves(self, symbol):
        lst = []
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col] == symbol:
                    if row > 0 and self.board[row-1][col] == ' ':
                        lst.append((row-1, col))
                    if row < 7 and self.board[row+1][col] == ' ':
                        lst.append((row+1, col))
                    if col > 0 and self.board[row][col-1] == ' ':
                        lst.append((row, col-1))
                    if col < 7 and self.board[row][col+1] == ' ':
                        lst.append((row, col+1))
        return lst
    
    def get_flip_moves(self,c):
        valid_moves = []
        for row in range(self.n):
            for col in range(self.n):
                if self.valid_move(row, col, c):
                    valid_moves.append((row, col))
        return valid_moves

    def flip(self, lst, c):
        for x,y in lst:
            self.board[x][y] = c

    def valid_move(self, x, y, c):
        opp = 'w' if c == 'b' else 'b'
        flag = False
        lst = []

        # go right
        if y < 7 and self.board[x][y+1] == opp:
            startX = x
            startY = y+2
            while(startY < 7) and (self.board[startX][startY] == opp):
                startY += 1
            
            if (startY < 7) and (self.board[startX][startY] == c): #encloses
                flag = True
                for i in range(y+1, startY):
                    lst.append((x, i))

        # go up
        if x > 0 and self.board[x-1][y] == opp:
            startX = x-2
            startY = y
            while(startX > 0) and (self.board[startX][startY] == opp):
                startX -= 1
            
            if (startX > 0) and (self.board[startX][startY] == c): #encloses
                flag = True
                for i in range(x-1, startX, -1):
                    lst.append((i, y))

        # go down
        if x < 7 and self.board[x+1][y] == opp:
            startX = x+2
            startY = y
            while(startX < 7) and (self.board[startX][startY] == opp):
                startX += 1
            
            if(startX < 7) and (self.board[startX][startY] == c): #encloses
                flag = True
                for i in range(x+1, startX):
                    lst.append((i, y))

        # go left
        if y > 0 and self.board[x][y-1] == opp:
            startX = x
            startY = y-2
            while(startY > 0) and (self.board[startX][startY] == opp):
                startY -= 1
            
            if(startY > 0) and (self.board[startX][startY] == c): #encloses
                flag = True
                for i in range(y-1, startY, -1):
                    lst.append((x, i))
        if(flag):
            return lst
        return []


    def end_of_game(self, players):
        if players[0].coins == 0 or players[1].coins == 0:
            return True
        return False
    
    def get_board(self):
        return self.board
    
    def set_board(self, board):
        self.board = board