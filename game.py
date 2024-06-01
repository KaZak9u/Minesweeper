import pygame
from board import Board


class Game:
    def __init__(self, block_length, dimensions, num_rows, num_cols, num_bombs):
        self.clock = pygame.time.Clock()
        self.block_length = block_length
        self.dimensions = dimensions
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.screen = pygame.display.set_mode(self.dimensions)
        self.num_bombs = num_bombs
        if dimensions[0] == 750:
            self.num_of_spaces = 79
        if dimensions[0] == 700:
            self.num_of_spaces = 70
        if dimensions[0] == 1200:
            self.num_of_spaces = 145

    def run(self):
        time = ""
        start_ticks = pygame.time.get_ticks()
        pygame.display.set_caption(f'Bombs: {str(0)} / {str(self.num_bombs)}{" " * self.num_of_spaces}00:00:00')
        board = Board(self.num_rows, self.num_cols, self.block_length)
        board.generate_board(self.num_bombs)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if event.button == 1:
                        board.discover_fields(x // self.block_length, y // self.block_length)
                        if board.blocks_matrix[x // self.block_length][y // self.block_length].exploded:
                            running = False
                    if event.button == 3:
                        board.mark_field(x // self.block_length, y // self.block_length)
            time = self.calculate_time(start_ticks)
            pygame.display.set_caption(f'Bombs: {str(board.count_marked())} / {str(self.num_bombs)}'
                                       f'{" " * self.num_of_spaces}{time}')
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE]:
                running = False
            pygame.display.flip()
            board.draw_window(self.screen)
            self.clock.tick(60)
        pygame.quit()
        return board.check_if_won(), time

    def calculate_time(self, start_ticks):
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"