from Game import *

def main():
    global game
    game = GameManager()
    game.gameInit()
    game.gameStart()


if __name__ == '__main__':
    main()