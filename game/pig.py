from gameplay import Game
import shell


def main():

    print('            88            ')
    print()
    print('8b,dPPYba,  88  ,adPPYb,d8')                       
    print('88P"    "8a 88 a8"    "Y88')
    print('88       d8 88 8b       88')
    print('88b,   ,a8" 88 "8a,   ,d88 ')
    print('88`YbbdP""  88  ""YbbdP"Y8')
    print('88              aa,    ,88 ')
    print('88               "Y8bbdP"')
    print('')

    player = input("What is your name? ")
    print()
    print(f"Welcome {player}! Let's pass some pigs")

    shell.Shell().cmdloop()


if __name__ == "__main__":
    main()
