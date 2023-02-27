from player import Player
import pickle


class Highscore():

    def __init__(self):
        high_score_file = open('high_score_file.bin', 'rb')
        high_score_dict = pickle.load(high_score_file)
        high_score_file.close()

    def get_high_score(self, high_score_dict):
        for i in high_score_dict:
            print(high_score_dict[i])

    def save(self, high_score_dict):
        name = Player.get_name()
        score = Player.get_score()
        high_score_dict[name] = score
        high_score_file = open('high_score_file.bin', 'wb')
        pickle.dump(high_score_dict, high_score_file)
        high_score_file.close()
