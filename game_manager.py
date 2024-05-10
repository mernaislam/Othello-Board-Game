from board import Board
from computer_player import ComputerPlayer
from gui import OthelloGUI
import copy


class GameManager:
    def __init__(self):
        self.board = Board()
        self.main_gui = OthelloGUI(self)
        self.computer_player = ComputerPlayer()
        self.main_gui.update_GUI_board(self.board.board, self.board.get_flip_moves('b'))
        self.main_gui.__del__()
    
    def main(self, x, y):
        if self.can_move('b'):
            if not self.valid_move(x, y, 'b'):
                return
            self.board.update_board(x, y, 'b')
            self.main_gui.update_GUI_board(self.board.board, [])
            self.board.players[0].coins -= 1

        if self.can_move('w'):
            x, y = self.computer_player.make_move(copy.deepcopy(self.board))
            self.board.update_board(x, y, 'w')
            self.main_gui.update_GUI_board(self.board.board, self.board.get_flip_moves('b'))
            self.board.players[1].coins -= 1
            while not self.can_move('b') and self.can_move('w'):
                x, y = self.computer_player.make_move(copy.deepcopy(self.board))
                self.board.update_board(x, y, 'w')
                self.main_gui.update_GUI_board(self.board.board, self.board.get_flip_moves('b'))
                self.board.players[1].coins -= 1

        self.board.update_score(self.board.players)
        self.main_gui.update_dashboard(self.board.players[0].score, self.board.players[1].score, self.board.players[0].coins, self.board.players[1].coins)
        
        if self.can_move('b'):
            return
        
        if self.board.players[0].score > self.board.players[1].score:
            self.main_gui.show_winner("You Won!")
        elif self.board.players[0].score < self.board.players[1].score:
            self.main_gui.show_winner("Computer Won!")
        else:
            self.main_gui.show_winner("It's a Draw!")

    def can_move(self, c):
        return self.board.get_flip_moves(c) != []

    def valid_move(self, x, y, c):
        return self.board.valid_move(x, y, c) != []
    
gm = GameManager()