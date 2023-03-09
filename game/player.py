"""Player Class, that player objects can be created from."""


class Player():
    """Creating Player class."""

    def __init__(self, name):
        """Init player."""
        self.name = name
        self.wins = 0
        self.roll_score = 0
        self.turn_score = 0
        self.total_score = 0
        self.games_played = 0

    def get_name(self):
        """Return the players name."""
        return self.name

    def set_name(self, new_name):
        """Set the players name."""
        self.name = new_name

    def get_wins(self):
        """Return the players wins."""
        return self.wins

    def set_wins(self, new_wins):
        """Set the players wins."""
        self.wins = new_wins

    def add_win(self):
        """Add one win to a player."""
        self.wins += 1

    def get_roll_score(self):
        """Return roll_score."""
        return self.roll_score

    def set_roll_score(self, new_roll_score):
        """Set roll_score."""
        self.roll_score = new_roll_score

    def get_turn_score(self):
        """Return turn_score."""
        return self.turn_score

    def set_turn_score(self, new_turn_score):
        """Set turn_score."""
        self.turn_score = new_turn_score

    def get_total_score(self):
        """Return total_score."""
        return self.total_score

    def set_total_score(self, new_total_score):
        """Set total score."""
        self.total_score = new_total_score

    def get_games_played(self):
        """Return games_played."""
        return self.games_played

    def set_games_played(self, new_games_played):
        """Set games_played."""
        self.games_played = new_games_played

    def add_games_played(self):
        """Add one game played to a player."""
        self.games_played += 1

    def clear_player_stats(self, player):
        """Set a players stats to 0."""
        player.set_wins(0)
        player.set_games_played(0)
