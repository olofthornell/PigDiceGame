class Player():

    def __init__(self, name, wins, roll_score, turn_score, total_score):
        self.name = name
        self.wins = 0
        self.roll_score = 0
        self.turn_score = 0
        self.total_score = 0

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_score(self):
        return self.score

    def set_score(self, new_score):
        self.score = new_score
