
class Board:
    def __init__(self):
        self.n = 8
        self.board = [[' ' for _ in range(self.n)] for _ in range(self.n)]
        self.board[3][3] = 'w'
        self.board[3][4] = 'b'
        self.board[4][4] = 'w'
        self.board[4][3] = 'b'

    def update_board(self, x, y):
        self.board[x][y] = 'b'

    def update_score(self):
        pass

    def display_valid_moves(self):
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col] == 'w':
                    if self.board[row-1][col] == ' ' and row > 0:
                        self.board[row-1][col] = 'h'
                    if self.board[row+1][col] == ' ' and row < 7:
                        self.board[row+1][col] = 'h'
                    if self.board[row][col-1] == ' ' and col > 0:
                        self.board[row][col-1] = 'h'
                    if self.board[row][col+1] == ' ' and col < 7:
                        self.board[row][col+1] = 'h'


    def valid_move(self):
        pass

    def end_of_game(self):
        pass