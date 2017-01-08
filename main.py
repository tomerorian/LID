import pygame
from random import randint
from Game import Game
from GameGrid import GameGrid
from Block import *

def debug_random_moving_blocks(blocks, game):
    for i in range(0, 5000):
        block = None
        while block is None:
            block = MovingBlock(game, \
                randint(0, game.grid.get_width()), \
                randint(0, game.grid.get_width()), \
                (randint(0, 255), randint(0, 255), randint(0, 255)), \
                1)
            if game.grid.add(block.x, block.y, block):
                blocks.append(block)
            else:
                block = None

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 1024))
    done = False

    game = Game(screen, GameGrid(screen))

    clock = pygame.time.Clock()

    blocks = []
    debug_random_moving_blocks(blocks, game)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                done = True
	        
        screen.fill((0, 0, 0))
        
        [block.tick() for block in blocks]
        [block.draw() for block in blocks]
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()