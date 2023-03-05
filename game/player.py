class Player():

    def __init__(self, name):
        """Initiating """
        self.name = name
        self.wins = 0
        self.roll_score = 0
        self.turn_score = 0
        self.total_score = 0
        self.games_played = 0

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_wins(self):
        return self.wins

    def set_wins(self, new_wins):
        self.wins = new_wins

    def add_win(self):
        self.wins += 1

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

    def get_games_played(self):
        return self.games_played

    def set_games_played(self, new_games_played):
        self.games_played = new_games_played

    def add_games_played(self):
        self.games_played += 1
