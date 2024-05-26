import pygame
from game import Game

pygame.init()
pygame.font.init()


BLOCK_LENGTH = 75
DIMENSIONS = (750, 750)
num_of_blocks_x = 10
num_of_blocks_y = 10
num_of_bombs = 4


def main():
    game = Game(BLOCK_LENGTH, DIMENSIONS, num_of_blocks_x, num_of_blocks_y, num_of_bombs)
    game.run()


if __name__ == "__main__":
    main()
