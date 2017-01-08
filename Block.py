from random import randint
import pygame
from Game import BLOCK_DIMENTION

class Block:
    def __init__(self, game, x, y, color):
        self._game = game
        self.x = x
        self.y = y
        self.color = color

    def tick(self):
        pass

    def draw(self):
        pygame.draw.rect(self._game.screen, self.color, pygame.Rect(self._game.grid.grid2screen(self.x), self._game.grid.grid2screen(self.y), BLOCK_DIMENTION, BLOCK_DIMENTION))


class MoveableBlock(Block):
    def __init__(self, game, x, y, color):
        Block.__init__(self, game, x, y, color)

    def move(self, x, y):
        if self._game.grid.move(self.x, self.y, x, y):
            self.x = x
            self.y = y
            return True

        return False


class MovingBlock(MoveableBlock):
    def __init__(self, game, x, y, color, speed):
        MoveableBlock.__init__(self, game, x, y, color)

        self._speed = speed
        self._xdir = 0
        self._ydir = 0

        while self._xdir == 0 and self._ydir == 0:
            self._xdir = randint(-1, 1)
            self._ydir = randint(-1, 1)

    def tick(self):
        x = self.x + self._xdir * self._speed
        y = self.y + self._ydir * self._speed

        if self._game.grid.move(self.x, self.y, x, y):
            self.x = x
            self.y = y
        else:
            self._xdir = 0
            self._ydir = 0

            while self._xdir == 0 and self._ydir == 0:
                self._xdir = randint(-1, 1)
                self._ydir = randint(-1, 1)