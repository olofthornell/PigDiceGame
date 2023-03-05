from player import Player
from high_score import High_score


def main():
    high_score = High_score()
    player1 = Player("Olof")
    player2 = Player("Görel")

    player1.add_games_played()
    player2.add_games_played()
    player1.add_win()

    player1.add_games_played()
    player2.add_games_played()
    player1.add_win()

    player1.add_games_played()
    player2.add_games_played()
    player2.add_win()

    print(player1.get_name())
    print(player1.get_wins())
    print(high_score.get_high_score())


if __name__ == "__main__":
    main()
