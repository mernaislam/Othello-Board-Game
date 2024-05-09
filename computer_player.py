from player import Player
import copy

class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()
        self.depth = 6 
        self.score = 2
        self.coins = 30

    def make_move(self, board):
        self.coins -= 1
        score, best_move = self.alpha_beta(board, self.depth, float("-inf"), float("inf"), True)
        print(best_move)
        if best_move != ():
            board.update_board(best_move[0], best_move[1], 'w')
        # return best_move

    def evaluate(self, board):
        score1 = board.players[0].score
        score2 = board.players[1].score
        s = score1 - score2
        return s

    def alpha_beta(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.end_of_game(board.players):
            return self.evaluate(board), None

        best_move = ()
        if maximizing_player:
            max_eval = float('-inf')
            for move in board.get_flip_moves('w'):
                tmp = copy.deepcopy(board.get_board())
                board.update_board(move[0], move[1], 'w') #do
                eval, _ = self.alpha_beta(board, depth - 1, alpha, beta, False) #recurse 
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                board.update_score(board.players)
                # board.board[move[0]][move[1]] = ' ' #undo 
                board.set_board(tmp) #undo
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in board.get_flip_moves('b'):
                tmp = copy.deepcopy(board.get_board())
                board.update_board(move[0], move[1], 'b')
                eval, _ = self.alpha_beta(board, depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                board.update_score(board.players)
                # board.board[move[0]][move[1]] = ' '
                board.set_board(tmp) #undo
                if beta <= alpha:
                    break
            return min_eval, best_move

