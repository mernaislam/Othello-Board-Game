
class Board:
    def __init__(self):
        self.n = 8
        self.board = [[' ' for _ in range(self.n)] for _ in range(self.n)]
        self.board[3][3] = 'w'
        self.board[3][4] = 'b'
        self.board[4][4] = 'w'
        self.board[4][3] = 'b'

    def update_board(self, x, y):
        if self.valid_move(x,y):
            self.board[x][y] = 'b'
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

    def display_valid_moves(self):
        # adjacent to white coins (left, up, right, bottom)
        hintPlaces = [[' ' for _ in range(self.n)] for _ in range(self.n)]
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col] == 'w':
                    if row > 0 and self.board[row-1][col] == ' ':
                        hintPlaces[row-1][col] = 'h'
                    if row < 7 and self.board[row+1][col] == ' ':
                        hintPlaces[row+1][col] = 'h'
                    if col > 0 and self.board[row][col-1] == ' ':
                        hintPlaces[row][col-1] = 'h'
                    if col < 7 and self.board[row][col+1] == ' ':
                        hintPlaces[row][col+1] = 'h'
        return hintPlaces

    def valid_move(self, row, col):   # b w w w b 
        # check if it flips coins
        # need to implement for computer player
        list = [1, -1]
        
        for i in range(2):
            black = 0
            # go right
            if self.board[row][col + list[i]] == 'w':  
                c = col + 2 * list[i]
                r = row
                while self.board[r][c] != 'w' or c < 0 or c > 7:
                    if self.board[r][c] == 'b':
                        black = 1
                        break
                    c = c + list[i]
                if black:
                    for i in range(col + list[i], c, list[i]):
                        self.board[row][i] = 'b'    

        # go up
        for i in range(2):
            if self.board[row + list[i]][col] == 'w': 
                r = row + 2 * list[i]
                c = col  
                while self.board[r][c] != 'w' or r < 0 or r > 7:
                    if self.board[r][c] == 'b':
                        black = 1
                        break
                    r = r + list[i]
                if black:
                    for i in range(row + list[i], r, list[i]):
                        self.board[i][col] = 'b'   
        if(black):
            return True
        else: 
            return False

    def end_of_game(self, player1, player2):
        if player1.coins == 0 or player2.coins == 0:
            return True
        return False