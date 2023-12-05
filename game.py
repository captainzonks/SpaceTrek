from game_states.explore_state import ExploreState
from ship import Ship
from space import Space


class Game:
    def __init__(self):
        self.space_size = (10, 10)
        self.space = Space(self.space_size)
        self.ship = Ship(self.space)
        self.is_running = True
        self.stack = []

        self.default_state = ExploreState(self)
        self.stack.append(self.default_state)

        self.space.initialize_space(self.space_size)

    def handle_input(self):
        self.stack[-1].handle_input()

    def push_new_state(self, state):
        self.stack.append(state)
        print()
        print("Entering", self.stack[-1].title)
        print()

    def pop_state_off_stack(self):
        self.stack.pop(-1)
        print()
        print("Entering", self.stack[-1].title)
        print()
