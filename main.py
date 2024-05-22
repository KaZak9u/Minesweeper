import pygame
from game import Game

pygame.init()
pygame.font.init()


BLOCK_LENGTH = 100
DIMENSIONS = (600, 600)
num_of_blocks_x = 6
num_of_blocks_y = 6
num_of_bombs = 4


def main():
    game = Game(BLOCK_LENGTH, DIMENSIONS, num_of_blocks_x, num_of_blocks_y, num_of_bombs)
    game.run()


if __name__ == "__main__":
    main()
