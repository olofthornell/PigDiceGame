import pickle


class High_score():

    def __init__(self):
        self.high_score_dict = {}
        try:
            with open('high_score_file.bin', 'rb') as high_score_file:
                self.high_score_dict = pickle.load(high_score_file)
        except (EOFError, FileNotFoundError):
            try:
                with open('high_score_file.bin', 'wb') as high_score_file:
                    pass
            except (FileNotFoundError):
                with open('high_score_file.bin', 'wb') as high_score_file:
                    pass

    def move_player_info(self, player, player_name):
        player.set_games_played(self.high_score_dict[player_name][0])
        player.set_wins(self.high_score_dict[player_name][1])

    def get_high_score(self):
        print(f"{'Name':<20}", end="")
        print(f"{'Wins':<20}", end="")
        print(f"{'Games played':<20}")
        for name in self.high_score_dict:
            print(f"{name:<20}", end="")
            print(f"{self.high_score_dict[name][1]:<20}", end="")
            print(self.high_score_dict[name][0])

    def save_current(self, player):
        name = player.get_name()
        games_played = player.get_games_played()
        wins = player.get_wins()
        games_wins_list = [games_played, wins]
        self.high_score_dict[name] = games_wins_list

    def save(self):
        with open('high_score_file.bin', 'wb') as high_score_file:
            pickle.dump(self.high_score_dict, high_score_file)

    def clear_dict(self):
        print("Are you sure you want to clear the high score list?" +
              "\n" + "This can not be undone!")
        option = input("(y/n):")
        if option.lower() == "y":
            self.high_score_dict.clear()
            print("The high score list was deleted.")
        else:
            print("The high score list was not deleted.")

    def delete_name(self, old_name):
        if old_name in self.high_score_dict:
            del self.high_score_dict[old_name]
