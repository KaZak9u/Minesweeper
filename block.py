import pygame

UNDISCOVERED_BLOCK_IMAGE = pygame.image.load("Assets/undiscovered_block.png")
EMPTY_BLOCK_IMAGE = pygame.image.load("Assets/empty_block.png")
MARKED_BLOCK_IMAGE = pygame.image.load("Assets/marked_box.png")
EMPTY_1_IMAGE = pygame.image.load("Assets/empty_1.png")
EMPTY_2_IMAGE = pygame.image.load("Assets/empty_2.png")
EMPTY_3_IMAGE = pygame.image.load("Assets/empty_3.png")
EMPTY_4_IMAGE = pygame.image.load("Assets/empty_4.png")
EMPTY_5_IMAGE = pygame.image.load("Assets/empty_5.png")
EMPTY_6_IMAGE = pygame.image.load("Assets/empty_6.png")
EMPTY_7_IMAGE = pygame.image.load("Assets/empty_7.png")
EMPTY_8_IMAGE = pygame.image.load("Assets/empty_8.png")
BOMBED_BLOCK_IMAGE = pygame.image.load("Assets/bombed_block.png")


class Block(object):  # Represent a single field on the board
    def __init__(self, bombed, size):
        self.image = UNDISCOVERED_BLOCK_IMAGE
        self.bombed = bombed
        self.neighbouring_bombs_num = 0
        self.size = size
        self.discovered = False
        self.marked = False
        self.exploded = False

    def set_neighbouring_bombs_num(self, neighbouring_bombs_num):
        self.neighbouring_bombs_num = neighbouring_bombs_num

    def mark(self):  # Changes the state and image when the block is marked or unmarked as a mine
        if not self.discovered:
            if self.marked:
                self.image = UNDISCOVERED_BLOCK_IMAGE
                self.marked = False
            else:
                self.image = MARKED_BLOCK_IMAGE
                self.marked = True

    def discover(self):  # Changes state and image after discovering block
        self.discovered = True
        match self.neighbouring_bombs_num:
            case 0:
                if self.bombed:
                    self.image = BOMBED_BLOCK_IMAGE
                    self.exploded = True
                else:
                    self.image = EMPTY_BLOCK_IMAGE
            case 1:
                self.image = EMPTY_1_IMAGE
            case 2:
                self.image = EMPTY_2_IMAGE
            case 3:
                self.image = EMPTY_3_IMAGE
            case 4:
                self.image = EMPTY_4_IMAGE
            case 5:
                self.image = EMPTY_5_IMAGE
            case 6:
                self.image = EMPTY_6_IMAGE
            case 7:
                self.image = EMPTY_7_IMAGE
            case 8:
                self.image = EMPTY_8_IMAGE
            case _:
                self.image = BOMBED_BLOCK_IMAGE
