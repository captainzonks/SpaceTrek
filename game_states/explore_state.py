from game_state import GameState
from game_states.encounter_state import EncounterState


class ExploreState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.title = 'Exploration'

    def handle_input(self):
        player_input = input().lower()

        match player_input:
            case 'w' | 's' | 'a' | 'd' | 'e' | 'p':
                self.game.ship.handle_ship_commands(player_input)
            case 'f':
                if self.game.ship.position.encounter is not None:
                    # engage encounter
                    self.game.push_new_state(
                        EncounterState(self.game, self.game.ship.position.encounter.encounter_type))
                else:
                    print("Cannot engage nothing!")
            case 'm':
                self.print_menu()
            case 'q':
                exit(0)
            case _:
                print("Invalid input")

    def print_menu(self):
        print('------EXPLORATION-------')
        print('     SHIP CONTROLS')
        print('|| WASD: Movement')
        print('|| E: Scan')
        print('|| F: Engage')
        print('|| Q: Quit Game')
        print('------------------------')
