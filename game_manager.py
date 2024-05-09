from board import Board
from computer_player import ComputerPlayer
from player import Player


class GameManager:
    def __init__(self):
        self.board = Board()
        self.players = [Player(), ComputerPlayer()]
