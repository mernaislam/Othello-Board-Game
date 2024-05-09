from player import Player

class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()
        self.depth = 0 
        self.score = 2
        self.coins = 30

    def make_move(self, board):
        best_move = self.alpha_beta(board, self.depth, float("-inf"), float("inf"), True)
        return best_move

    def evaluate(self, board):
        pass

    def alpha_beta(self, board, depth, alpha, beta, maximizing_player):
        pass