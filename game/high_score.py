from player import Player
import pickle


class High_score():

    def __init__(self):
        high_score_file = open('high_score_file.bin', 'rb')
        self.high_score_dict = pickle.load(high_score_file)
        high_score_file.close()

    def get_high_score(self):
        for i in self.high_score_dict:
            print(self.high_score_dict[i])

    def save(self):
        name = Player.get_name()
        score = Player.get_score()
        self.high_score_dict[name] = score
        high_score_file = open('high_score_file.bin', 'wb')
        pickle.dump(self.high_score_dict, high_score_file)
        high_score_file.close()
