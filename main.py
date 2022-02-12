from game import Game

def main():
    user_name = Game.get_user_name()
    game = Game(user_name)
    game.play()

if __name__ == '__main__':
    main()
    