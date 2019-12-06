from Game import Game

def main():
    game = Game()
    game.init()
    game.setPlayerNames(("Thomas", "Seb"))
    game.run()

main()