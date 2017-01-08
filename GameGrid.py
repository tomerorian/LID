from collections import defaultdict
from Game import BLOCK_DIMENTION, FOOD_UUID
from Cell import Cell
from Food import Food

class GameGrid:
    def __init__(self, screen):
        self._screen = screen
        self._grid = defaultdict(lambda : defaultdict(lambda: None))

    def move(self, from_x, from_y, to_x, to_y):
        if to_x < 0 or to_x >= self.get_width() or to_y < 0 or to_y >= self.get_height():
            return False

        if self._grid[to_x][to_y] is not None:
            return False

        self._grid[to_x][to_y] = self._grid[from_x][from_y]
        self._grid[from_x][from_y] = None

        return True

    def add(self, x, y, obj):
        if self._grid[x][y] is not None:
            return False

        self._grid[x][y] = obj

        return True

    def grid2screen(self, xy):
        return xy * BLOCK_DIMENTION

    def get_width(self):
        return self._screen.get_width() / BLOCK_DIMENTION

    def get_height(self):
        return self._screen.get_height() / BLOCK_DIMENTION

    def get(self, x, y):
        if self._grid[x][y] is None:
            return None

        return self._grid[x][y]