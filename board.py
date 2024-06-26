import pygame
import random
from block import Block


class Board(object):  # Represents the board containing fields
    def __init__(self, num_rows, num_cols, block_length):
        self.blocks_matrix = []
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.block_length = block_length

    # Generates a list containing indexes of where bombs should be placed on the board
    def generate_random_bombed_fields_list(self, bombs_num):
        fields_list = []
        for i in range(bombs_num):
            flag = False
            while not flag:
                rand_num = random.randint(0, self.num_rows * self.num_cols)
                if rand_num not in fields_list:
                    fields_list.append(rand_num)
                    flag = True
        return fields_list

    # Fills the board with blocks
    def fill_board_with_blocks(self, bombed_fields_list):
        for i in range(self.num_rows):
            self.blocks_matrix.append([])
            for j in range(self.num_cols):
                if i * self.num_cols + j in bombed_fields_list:
                    self.blocks_matrix[i].append(Block(True, self.block_length))
                else:
                    self.blocks_matrix[i].append(Block(False, self.block_length))

    # Counts how many neighbouring blocks are bombed for a given indexes of matrix
    def count_neighbours(self, i, j):
        num = 0
        if i > 0:
            if self.blocks_matrix[i - 1][j].bombed:
                num += 1
            if j > 0:
                if self.blocks_matrix[i - 1][j - 1].bombed:
                    num += 1
            if j < len(self.blocks_matrix[i - 1]) - 1:
                if self.blocks_matrix[i - 1][j + 1].bombed:
                    num += 1
        if i < len(self.blocks_matrix) - 1:
            if self.blocks_matrix[i + 1][j].bombed:
                num += 1
            if j > 0:
                if self.blocks_matrix[i + 1][j - 1].bombed:
                    num += 1
            if j < len(self.blocks_matrix[i + 1]) - 1:
                if self.blocks_matrix[i + 1][j + 1].bombed:
                    num += 1
        if j > 0:
            if self.blocks_matrix[i][j - 1].bombed:
                num += 1
        if j < len(self.blocks_matrix[i]) - 1:
            if self.blocks_matrix[i][j + 1].bombed:
                num += 1
        return num

    # Sets number of neighbouring bombs for every block on the board
    def set_num_of_neighbours_on_board(self):
        for i in range(len(self.blocks_matrix)):
            for j in range(len(self.blocks_matrix[i])):
                if not self.blocks_matrix[i][j].bombed:
                    self.blocks_matrix[i][j].set_neighbouring_bombs_num(self.count_neighbours(i, j))

    # Preprocesses the board before game
    def generate_board(self, bombs_num):
        bombed_fields_list = self.generate_random_bombed_fields_list(bombs_num)
        self.fill_board_with_blocks(bombed_fields_list)
        self.set_num_of_neighbours_on_board()

    # Checks if the player correctly identified every bomb on the board
    def check_if_won(self):
        for line in self.blocks_matrix:
            for block in line:
                if block.bombed and not block.marked:
                    return False
        return True

    # Recursive function that discovers all the fields without neighbouring bombs that are neighbouring to field
    # discovered by player
    def discover_fields(self, i, j):
        self.blocks_matrix[i][j].discover()
        if self.blocks_matrix[i][j].neighbouring_bombs_num == 0:
            if i > 0:
                if not (self.blocks_matrix[i - 1][j].bombed or self.blocks_matrix[i - 1][j].discovered):
                    self.discover_fields(i - 1, j)
            if i < len(self.blocks_matrix) - 1:
                if not (self.blocks_matrix[i + 1][j].bombed or self.blocks_matrix[i + 1][j].discovered):
                    self.discover_fields(i + 1, j)
            if j > 0:
                if not (self.blocks_matrix[i][j - 1].bombed or self.blocks_matrix[i][j - 1].discovered):
                    self.discover_fields(i, j - 1)
            if j < len(self.blocks_matrix[i]) - 1:
                if not (self.blocks_matrix[i][j + 1].bombed or self.blocks_matrix[i][j + 1].discovered):
                    self.discover_fields(i, j + 1)

    # Displays current state of board on the screen
    def draw_window(self, screen):
        for i in range(len(self.blocks_matrix)):
            for j in range(len(self.blocks_matrix[i])):
                block_rect = pygame.Rect(i * self.block_length, j * self.block_length,
                                         self.block_length, self.block_length)
                screen.blit(pygame.transform.scale(self.blocks_matrix[i][j].image, (self.block_length, self.block_length)),
                            (block_rect.x, block_rect.y))
        pygame.display.update()

    def mark_field(self, i, j):
        self.blocks_matrix[i][j].mark()

    # Counts how man blocks are marked by player
    def count_marked(self):
        num = 0
        for i in self.blocks_matrix:
            for j in i:
                if j.marked:
                    num += 1
        return num
