class Player():

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.roll_score = 0
        self.turn_score = 0
        self.total_score = 0

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_wins(self):
        return self.score

    def set_wins(self, new_score):
        self.score = new_score

    def get_roll_score(self):
        return self.roll_score

    def set_roll_score(self, new_roll_score):
        self.roll_score = new_roll_score

    def get_turn_score(self):
        return self.turn_score

    def set_turn_score(self, new_turn_score):
        self.turn_score = new_turn_score

    def get_total_score(self):
        return self.total_score

    def set_total_score(self, new_total_score):
        self.total_score = new_total_score