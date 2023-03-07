from player import Player
from high_score import High_score


def main():
    high_score = High_score()
    player1 = Player("Hjärt-Ivar")
    player2 = Player("Görel")
    player3 = Player("Stig")

    player1.add_games_played()
    player2.add_games_played()
    player3.add_games_played()
    player1.add_win()

    player1.add_games_played()
    player2.add_games_played()
    player3.add_games_played()
    player1.add_win()

    player1.add_games_played()
    player2.add_games_played()
    player2.add_win()

    player1.add_games_played()
    player2.add_games_played()
    player3.add_games_played()
    player3.add_win()

    high_score.save_current(player1)
    high_score.save_current(player2)
    high_score.save_current(player3)
    high_score.get_high_score()
    high_score.clear_dict()
    high_score.save()


if __name__ == "__main__":
    main()
