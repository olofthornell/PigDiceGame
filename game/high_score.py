import pickle


class High_score():

    def __init__(self):
        self.high_score_dict = {}
        try:
            with open('game/high_score_file.bin', 'rb') as high_score_file:
                self.high_score_dict = pickle.load(high_score_file)
        except EOFError:
            with open('game/high_score_file.bin', 'wb') as high_score_file:
                pass
        except FileNotFoundError:
            with open('game/high_score_file.bin', 'wb') as high_score_file:
                pass

    def get_high_score(self):
        for i in self.high_score_dict:
            print(self.high_score_dict[i])

    def save_current(self, player):
        games_wins_list = [player.get_games_played, player.get_wins]
        self.high_score_dict[player.get_name] = games_wins_list

    def save(self, player):
        name = player.get_name()
        score = player.get_wins()
        self.high_score_dict[name] = score
        with open('game/high_score_file.bin', 'wb') as high_score_file:
            pickle.dump(self.high_score_dict, high_score_file)
