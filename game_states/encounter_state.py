from asteroid import Asteroid
from encounter import Encounter
from game_state import GameState
from space_station import SpaceStation


class EncounterState(GameState):
    def __init__(self, game, encounter_type):
        super().__init__(game)
        self.encounter_type: Encounter = encounter_type
        self.title = 'Encounter'
        self.menu = ()
        self.tools = []
        self.initialize_encounter()

    def handle_input(self):
        player_input = input().lower()

        match player_input:
            case '1':
                for entry in self.menu:
                    print(entry)
            case '2':
                print("Disengaging")
                self.game.pop_state_off_stack()
            case 'm':
                self.print_menu()
            case 'q':
                exit(0)
            case _:
                print("Invalid input")

    def print_menu(self):
        print('------ENCOUNTER-------')
        print('    SHIP CONTROLS')
        for entry in self.menu:
            print(entry)
        print('|| Q: Quit Game')
        print('-----------------------')

    def initialize_encounter(self):
        match self.encounter_type:
            case Asteroid():
                self.menu = ('|| 1: Mine', '|| 2: Disengage')
                # mining laser strength
                self.tools[0] = 150
            case SpaceStation():
                self.menu = ('|| 1: Dock', '|| 2: Disengage')
        self.encounter_type.tools = self.tools
