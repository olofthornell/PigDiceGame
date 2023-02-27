import player
import pickle


class highscore():

    def __init__(self):
        high_score_file = open('high_score_file.bin', 'rb')
        high_score_dict = pickle.load(high_score_file)
        high_score_file.close()


    def get_high_score(high_score_file):
        for i in high_score_file:
            print(high_score_file[i])



    def save(self, high_score_dict):
        high_score_dict[name] = score
        high_score_file = open('high_score_file.bin', 'wb')
        pickle.dump(high_score_dict, high_score_file)
        high_score_file.close()

