from encounters.asteroid import Asteroid
from game_state import GameState
from encounters.space_station import SpaceStation


class EncounterState(GameState):
    def __init__(self, game, encounter_type):
        super().__init__(game)
        self.encounter_type = encounter_type
        self.title = 'Encounter'
        self.menu = ()
        self.tools = []
        self.initialize_encounter()

    def handle_input(self):
        player_input = input().lower()

        match player_input:
            case '1':
                self.encounter_action()
            case '2':
                print("Disengaging")
                self.game.pop_state_off_stack()
            case 'm':
                self.print_menu()
            case 'q':
                exit(0)
            case _:
                print("Invalid input")

    def update(self):
        self.encounter_type.print()

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
                self.menu = ('|| 1: Mine', '|| 2: Leave')
                # mining laser strength
                self.tools.append(150)
            case SpaceStation():
                self.menu = ('|| 1: Sell Ore', '|| 2: Leave')
        self.encounter_type.tools = self.tools

    def encounter_action(self):
        match self.encounter_type:
            case Asteroid():
                mined = self.encounter_type.action(self.game.ship)
                self.game.ship.inventory.add_ore(mined)
            case SpaceStation():
                self.encounter_type.action(self.game.ship.inventory)
