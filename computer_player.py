from player import Player
import copy

class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()
        # self.depth = 5

    def make_move(self, board):
        score, best_move = self.alpha_beta(board, self.depth, float("-inf"), float("inf"), True)
        print(best_move)
        if best_move != None:
            board.update_board(best_move[0], best_move[1], 'w')
        else:
            best_move = board.get_flip_moves('w')[0]
        return best_move
    
    def open(self, row, col, board, c, direction):
        dx = 1 if direction == "down" else -1 if direction == "up" else 0
        dy = 1 if direction == "right" else -1 if direction == "left" else 0
        while 0 <= row < 8 and 0 <= col < 8 and board.board[row][col] == c:
            row += dx
            col += dy
        
        return 0 <= row < 8 and 0 <= col < 8 and board.board[row][col] == ' '
    
    def closed(self, row, col, board, c, direction):  
        dx = 1 if direction == "down" else -1 if direction == "up" else 0
        dy = 1 if direction == "right" else -1 if direction == "left" else 0
        opp = 'w' if c == 'b' else 'b'
        while 0 <= row < 8 and 0 <= col < 8 and board.board[row][col] == c:
            row += dx
            col += dy
        
        return 0 <= row < 8 and 0 <= col < 8 and board.board[row][col] == opp

    
    def strength(self, board, c):
        s = 0
        if board.end_of_game(board.players):
            board.update_score(board.players)
            if board.players[0].score < board.players[1].score:
                if c == 'w':
                    return 1000
                else:
                    return 0
        # count the main score
        for row in range(8):
            for col in range(8):
                if board.board[row][col] == c:
                    s += 3
                    if self.open(row, col, board, c, "up") and self.closed(row, col, board, c, "down") or self.closed(row, col, board, c, "up") and self.open(row, col, board, c, "down"):
                        s -= 1
                    if self.open(row, col, board, c, "left") and self.closed(row, col, board, c, "right") or self.closed(row, col, board, c, "left") and self.open(row, col, board, c, "right"):
                        s -= 1
        
        # count the corner score
        q = []
        visited = [[False for _ in range(8)] for _ in range(8)]
        if board.board[0][0] == c:
            q.append((0, 0))
            visited[0][0] = True
        if board.board[0][7] == c:
            q.append((0, 7))
            visited[0][7] = True
        if board.board[7][0] == c:
            q.append((7, 0))
            visited[7][0] = True
        if board.board[7][7] == c:
            q.append((7, 7))
            visited[7][7] = True
        
        while q != []:
            x, y = q.pop()
            s += 10
            if x < 7 and board.board[x+1][y] == c and not visited[x+1][y]:
                q.append((x+1, y))
                visited[x+1][y] = True
            if x > 0 and board.board[x-1][y] == c and not visited[x-1][y]:
                q.append((x-1, y))
                visited[x-1][y] = True
            if y < 7 and board.board[x][y+1] == c and not visited[x][y+1]:
                q.append((x, y+1))
                visited[x][y+1] = True
            if y > 0 and board.board[x][y-1] == c and not visited[x][y-1]:
                q.append((x, y-1))
                visited[x][y-1] = True
        
        return s

    def evaluate(self, board):
        return self.strength(board, 'w') - self.strength(board, 'b')

    def alpha_beta(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.end_of_game(board.players):
            return self.evaluate(board), None

        best_move = ()
        if maximizing_player:
            max_eval = float('-inf')

            flip_moves = board.get_flip_moves('w')

            if flip_moves == []:
                max_eval, _ = self.alpha_beta(board, depth - 1, alpha, beta, False)
                return max_eval, None
            
            best_move = flip_moves[0]
            
            for move in flip_moves:
                tmp = copy.deepcopy(board.get_board())
                board.update_board(move[0], move[1], 'w') #do
                eval, _ = self.alpha_beta(board, depth - 1, alpha, beta, False) #recurse 
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                board.update_score(board.players)
                board.set_board(tmp) #undo
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            flip_moves = board.get_flip_moves('b')

            if flip_moves == []:
                min_eval, _ = self.alpha_beta(board, depth - 1, alpha, beta, True)
                return min_eval, None
            
            best_move = flip_moves[0]

            for move in flip_moves:
                tmp = copy.deepcopy(board.get_board())
                board.update_board(move[0], move[1], 'b')
                eval, _ = self.alpha_beta(board, depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                board.update_score(board.players)
                board.set_board(tmp) #undo
                if beta <= alpha:
                    break
            return min_eval, best_move

