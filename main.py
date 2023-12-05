from game import Game

if __name__ == '__main__':
    game = Game()

    # initialize the ship's initial position
    game.ship.update_position(game.ship.previous_position.coordinates[0], game.ship.previous_position.coordinates[1])

    game.space.print()
    while game.is_running:
        print("Please enter your command (Press M for list):")
        game.handle_input()
        game.update()
