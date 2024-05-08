from board import Board
# from computer_player import ComputerPlayer
# from player import Player


class GameManager:
    def __init__(self):
        self.board = Board()
        # self.players = [Player(), ComputerPlayer()]

    # def runApp(self):
    #     self.board.display_valid_moves()
    #     self.gui.update_board(self.board.board, 8)
    #     print('ayhagaa')
    #     self.board.update_board(self.gui.get_x_move(), self.gui.yMove)
    #     print('ayhaga222')
    #     self.board.display_valid_moves()
    #     self.gui.update_board(self.board.board, 8)
