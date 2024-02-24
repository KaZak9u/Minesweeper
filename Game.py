import pygame
from Board import Board


class Game:
    def __init__(self, block_length, dimensions, num_rows, num_cols):
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.my_font = pygame.font.SysFont('Comic Sans MS', 100)
        self.text_win_surface = self.my_font.render('YOU WON!!!', False, (0, 210, 0))
        self.text_lose_surface = self.my_font.render('YOU LOST :(', False, (250, 0, 0))
        self.block_length = block_length
        self.dimensions = dimensions
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.screen = pygame.display.set_mode(self.dimensions)

    def run(self):
        board = Board(self.num_rows, self.num_cols, self.block_length)
        board.generate_board(10)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pygame.mouse.get_pos()
                        board.discover_fields(x // self.block_length, y // self.block_length)
                        # board.blocks_matrix[x // self.block_length][y // self.block_length].discover()
                    if event.button == 3:
                        x, y = pygame.mouse.get_pos()
                        board.mark_field(x // self.block_length, y // self.block_length)
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE]:
                running = False
            pygame.display.flip()
            board.draw_window(self.screen)
            self.clock.tick(60)
        if board.check_if_won():
            self.screen.blit(self.text_win_surface, (50, 300))
        else:
            self.screen.blit(self.text_lose_surface, (50, 300))
        pygame.display.update()
        pygame.quit()
