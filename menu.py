from buttons import *
from game import Game
from time_display import display_time
from records_saving import update_record

BACKGROUND_IMAGE = pygame.image.load("Assets/menu_background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (600, 600))

RULES_IMAGE = pygame.image.load("Assets/rules.png")
RULES = pygame.transform.scale(RULES_IMAGE, (600, 600))

ENDING_SCREEN_WON_IMAGE = pygame.image.load("Assets/ending_screen_won.png")
ENDING_SCREEN_WON = pygame.transform.scale(ENDING_SCREEN_WON_IMAGE, (600, 600))

ENDING_SCREEN_LOST_IMAGE = pygame.image.load("Assets/ending_screen_lost.png")
ENDING_SCREEN_LOST = pygame.transform.scale(ENDING_SCREEN_LOST_IMAGE, (600, 600))


GAME_SETTING = {
    "block_length": [75, 50, 50],
    "dimensions": [(750, 750), (700, 700), (1200, 800)],
    "num_of_blocks_x": [10, 14, 24],
    "num_of_blocks_y": [10, 14, 16],
    "num_of_bombs": [(1, 20, 30), (15, 25, 35), (30, 45, 60)]
}


class Menu:
    def __init__(self, flag):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.flag = flag

    def draw_menu(self, buttons, chosen_1, chosen_2, chosen_3, chosen_4):
        self.screen.blit(BACKGROUND, (0, 0))
        if chosen_1:
            self.screen.blit(buttons[0], BUTTON_1_RECT)
        else:
            self.screen.blit(buttons[1], BUTTON_1_RECT)
        if chosen_2:
            self.screen.blit(buttons[2], BUTTON_2_RECT)
        else:
            self.screen.blit(buttons[3], BUTTON_2_RECT)
        if chosen_3:
            self.screen.blit(buttons[4], BUTTON_3_RECT)
        else:
            self.screen.blit(buttons[5], BUTTON_3_RECT)
        if chosen_4:
            self.screen.blit(buttons[6], BUTTON_4_RECT)
        else:
            self.screen.blit(buttons[7], BUTTON_4_RECT)
        pygame.display.update()

    def check_collisions(self, buttons, mouse_pos):
        choices = [False, False, False, False]
        for index, rect in enumerate(BUTTON_RECTS):
            if rect.collidepoint(mouse_pos):
                choices[index] = True
        self.draw_menu(buttons, choices[0], choices[1], choices[2], choices[3])

    def menu_loop(self, buttons):
        choice = 0
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            self.check_collisions(buttons, mouse_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.flag = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for index, button in enumerate(BUTTON_RECTS):
                            if button.collidepoint(mouse_pos):
                                choice = index + 1
                                running = False
            self.clock.tick(60)
        return choice

    def start_game(self, dimension_choice, difficulty):
        block_length = GAME_SETTING["block_length"][dimension_choice]
        dimensions = GAME_SETTING["dimensions"][dimension_choice]
        num_of_blocks_x = GAME_SETTING["num_of_blocks_x"][dimension_choice]
        num_of_blocks_y = GAME_SETTING["num_of_blocks_y"][dimension_choice]
        num_of_bombs = GAME_SETTING["num_of_bombs"][dimension_choice][difficulty]
        game = Game(block_length, dimensions, num_of_blocks_x, num_of_blocks_y, num_of_bombs)
        result, time = game.run()
        self.run_ending_screen(result, time, dimension_choice, difficulty)

    def run_difficulty_choice_menu(self, dimension_choice):
        pygame.display.set_caption('Select difficulty')
        choice = self.menu_loop(DIFFICULTY_CHOICE_BUTTONS)
        if choice == 4:
            self.run_dimension_choice_menu()
        pygame.quit()
        if choice == 1:
            self.start_game(dimension_choice, 0)
        if choice == 2:
            self.start_game(dimension_choice, 1)
        if choice == 3:
            self.start_game(dimension_choice, 2)

    def run_dimension_choice_menu(self):
        pygame.display.set_caption('Select dimension')
        choice = self.menu_loop(DIMENSION_CHOICE_BUTTONS)
        if choice == 1:
            self.run_difficulty_choice_menu(0)
        if choice == 2:
            self.run_difficulty_choice_menu(1)
        if choice == 3:
            self.run_difficulty_choice_menu(2)
        if choice == 4:
            self.run_main_menu()

    def run_rules(self):
        pygame.display.set_caption('Rules')
        self.screen.fill((255, 255, 255))
        self.screen.blit(BACKGROUND, (0, 0))
        self.screen.blit(RULES, (0, 10))
        pygame.display.update()
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if BUTTON_4_RECT.collidepoint(mouse_pos):
                    self.screen.blit(BUTTON_BACK_CHOSEN_IMAGE, BUTTON_4_RECT)
                else:
                    self.screen.blit(BUTTON_BACK_IMAGE, BUTTON_4_RECT)
                pygame.display.update()
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if BUTTON_4_RECT.collidepoint(mouse_pos):
                            running = False
            self.clock.tick(60)
        self.run_main_menu()

    def run_main_menu(self):
        pygame.display.set_caption('Minesweeper menu')
        choice = self.menu_loop(MAIN_MENU_BUTTONS)
        if choice == 1:
            self.run_dimension_choice_menu()
        if choice == 2:
            self.run_rules()
        if choice == 4:
            self.flag = False
        pygame.quit()

    def draw_ending_screen_buttons(self, main_menu_chosen, try_again_chosen):
        if main_menu_chosen:
            self.screen.blit(BUTTON_MAIN_MENU_CHOSEN, BUTTON_3_RECT)
        else:
            self.screen.blit(BUTTON_MAIN_MENU, BUTTON_3_RECT)
        if try_again_chosen:
            self.screen.blit(BUTTON_TRY_AGAIN_CHOSEN, BUTTON_2_RECT)
        else:
            self.screen.blit(BUTTON_TRY_AGAIN, BUTTON_2_RECT)
        pygame.display.update()

    def check_ending_screen_buttons(self, mouse_pos, result, time):
        if result:
            self.screen.blit(ENDING_SCREEN_WON, (0, 0))
            display_time(self.screen, time, 140, 180, (32, 40))
        else:
            self.screen.blit(ENDING_SCREEN_LOST, (0, 0))
        try_again_chosen = False
        main_menu_chosen = False
        if BUTTON_2_RECT.collidepoint(mouse_pos):
            try_again_chosen = True
        if BUTTON_3_RECT.collidepoint(mouse_pos):
            main_menu_chosen = True
        self.draw_ending_screen_buttons(main_menu_chosen, try_again_chosen)

    def run_ending_screen(self, result, time, dimension_choice, difficulty):
        pygame.init()
        pygame.display.set_caption("Ending screen")
        self.screen = pygame.display.set_mode((600, 600))

        choice = 0

        if result:
            update_record(dimension_choice, difficulty, time)

        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            self.check_ending_screen_buttons(mouse_pos, result, time)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if BUTTON_2_RECT.collidepoint(mouse_pos):
                            choice = 1
                            running = False
                        if BUTTON_3_RECT.collidepoint(mouse_pos):
                            running = False
        if choice == 1:
            self.start_game(dimension_choice, difficulty)
        pygame.quit()


if __name__ == "__main__":
    menu = Menu(True)
    menu.run_main_menu()
