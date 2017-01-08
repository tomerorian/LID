from Game import *
from Block import *

class Food(Block):
    def __init__(self, game, x, y, value):
        Block.__init__(self, game, x, y, (0, 255, 0))

        self.value = value
        self.uuid = FOOD_UUID