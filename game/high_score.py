import player
import pickle


class highscore():

    def __init__(self):
        highscorefile = open('highscorefile.bin', 'rb')
        highscore_dict = pickle.load(highscorefile)
        highscorefile.close()


    def get_highscore(highscorefile):
        for i in highscorefile:
            print(highscorefile[i])



    def save(self, highscore_dict):
        highscore_dict[name] = score
        highscorefile = open('highscorefile.bin', 'wb')
        pickle.dump(highscore_dict, highscorefile.bin)
        highscorefile.close()

