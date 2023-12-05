class Inventory:
    def __init__(self):
        self.storage_size = 10000
        self.stuff = []
        self.ore = 0
        self.money = 1000

    def add_ore(self, incoming_ore):
        self.ore += incoming_ore

    def subtract_ore(self, quantity_to_remove) -> int:
        if quantity_to_remove > self.ore:
            self.ore -= quantity_to_remove
            return quantity_to_remove
        else:
            to_be_returned = quantity_to_remove - self.ore
            self.ore = 0
            return to_be_returned
