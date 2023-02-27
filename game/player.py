class Player():

    def __init__(self, name, score):
        self.name = name
        self.score = 0

    def change_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def set_score(self, new_score):
        self.score = new_score
