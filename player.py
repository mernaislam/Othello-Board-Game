class Player:
    def __init__(self):
        self.coins = 30
        self.score = 2

    def make_move(self):
        self.coins -= 1