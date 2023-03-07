import pickle


class High_score():

    def __init__(self):
        self.high_score_dict = {}
        try:
            with open('game/high_score_file.bin', 'rb') as high_score_file:
                self.high_score_dict = pickle.load(high_score_file)
        except (EOFError, FileNotFoundError):
            try:
                with open('game/high_score_file.bin', 'wb') as high_score_file:
                    pass
            except (FileNotFoundError):
                with open('game/high_score_file.bin', 'wb') as high_score_file:
                    pass

    def move_player_info(self, player, player_name):
        player.set_games_played(self.high_score_dict[player_name][0])
        player.set_wins(self.high_score_dict[player_name][1])

    def get_high_score(self):
        print_name = "Name"
        print_games_played = "Games_played"
        print_wins = "Wins"
        print(f"{print_name:<20}", end="")
        print(f"{print_games_played:<20}", end="")
        print(f"{print_wins:<20}")
        for name in self.high_score_dict:
            print(f"{name:<20}", end="")
            print(f"{self.high_score_dict[name][0]:<20}", end="")
            print(self.high_score_dict[name][1])

    def save_current(self, player):
        name = player.get_name()
        games_played = player.get_games_played()
        wins = player.get_wins()
        games_wins_list = [games_played, wins]
        self.high_score_dict[name] = games_wins_list

    def save(self):
        with open('game/high_score_file.bin', 'wb') as high_score_file:
            pickle.dump(self.high_score_dict, high_score_file)

    def clear_dict(self):
        print("Are you sure you want to clear the high score list?" +
              "\n" + "This can not be undone!")
        option = input("(Y/N):")
        if option.upper() == "Y":
            self.high_score_dict.clear()
            print("The high score list was deleted.")
        else:
            print("The high score list was not deleted.")
