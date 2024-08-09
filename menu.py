from buttons import *
from game import Game
from time_display import display_time
from records_saving import update_record, load_records

MENU_SIZE = (600, 600)

BACKGROUND_IMAGE = pygame.image.load("assets/menu_background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, MENU_SIZE)

RULES_IMAGE = pygame.image.load("assets/rules.png")
RULES = pygame.transform.scale(RULES_IMAGE, MENU_SIZE)

HIGH_SCORES_TABLE_IMAGE = pygame.image.load("assets/high_scores_table.png")
HIGH_SCORES_TABLE = pygame.transform.scale(HIGH_SCORES_TABLE_IMAGE, MENU_SIZE)

ENDING_SCREEN_WON_IMAGE = pygame.image.load("assets/ending_screen_won.png")
ENDING_SCREEN_WON = pygame.transform.scale(ENDING_SCREEN_WON_IMAGE, MENU_SIZE)

ENDING_SCREEN_LOST_IMAGE = pygame.image.load("assets/ending_screen_lost.png")
ENDING_SCREEN_LOST = pygame.transform.scale(ENDING_SCREEN_LOST_IMAGE, MENU_SIZE)


GAME_SETTING = {
    "block_length": [75, 50, 50],
    "dimensions": [(750, 750), (700, 700), (1200, 800)],
    "num_of_blocks_x": [10, 14, 24],
    "num_of_blocks_y": [10, 14, 16],
    "num_of_bombs": [(10, 20, 30), (15, 25, 35), (30, 45, 60)]
}


class Menu:  # Represents menu outside the main game
    def __init__(self, flag):
        pygame.init()
        self.screen = pygame.display.set_mode(MENU_SIZE)
        self.clock = pygame.time.Clock()
        self.flag = flag

    # Displays on screen images of buttons provided in "buttons" list in positions of BUTTON_1,2,3,4
    # "buttons" list should contain 8 images, 2 for every button - chosen and default
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

    # Checks if mouse collides with any of the 4 buttons and draws default and chosen buttons on the screen
    def check_collisions(self, buttons, mouse_pos):
        choices = [False, False, False, False]
        for index, rect in enumerate(BUTTON_RECTS):
            if rect.collidepoint(mouse_pos):
                choices[index] = True
        self.draw_menu(buttons, choices[0], choices[1], choices[2], choices[3])

    # Loop that is used in main menu, dimensions selection and difficulty selection screens
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

    # Runs game with settings selected by player
    def start_game(self, dimension_choice, difficulty):
        block_length = GAME_SETTING["block_length"][dimension_choice]
        dimensions = GAME_SETTING["dimensions"][dimension_choice]
        num_of_blocks_x = GAME_SETTING["num_of_blocks_x"][dimension_choice]
        num_of_blocks_y = GAME_SETTING["num_of_blocks_y"][dimension_choice]
        num_of_bombs = GAME_SETTING["num_of_bombs"][dimension_choice][difficulty]
        game = Game(block_length, dimensions, num_of_blocks_x, num_of_blocks_y, num_of_bombs)
        result, time = game.run()
        self.run_ending_screen(result, time, dimension_choice, difficulty)

    # Runs difficulty choice screen
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

    # Runs dimension choice screen
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

    # Runs rules screen
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

    # Displays all the elements on high scores screen
    def draw_high_scores(self, back_chosen):
        self.screen.blit(BACKGROUND, (0, 0))
        self.screen.blit(HIGH_SCORES_TABLE, (0, 20))
        self.display_records_in_table()
        if back_chosen:
            self.screen.blit(BUTTON_BACK_CHOSEN_IMAGE, BUTTON_4_RECT)
        else:
            self.screen.blit(BUTTON_BACK_IMAGE, BUTTON_4_RECT)
        pygame.display.update()

    # Runs high scores window
    def run_high_scores(self):
        pygame.display.set_caption('High scores')
        self.screen.fill((255, 255, 255))

        back = False

        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            if BUTTON_4_RECT.collidepoint(mouse_pos):
                self.draw_high_scores(True)
            else:
                self.draw_high_scores(False)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.flag = False
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if BUTTON_4_RECT.collidepoint(mouse_pos):
                            back = True
                            running = False
            self.clock.tick(60)
        if back:
            self.run_main_menu()

    # Displays proper time lengths in table in high scores screen
    def display_records_in_table(self):
        start_x = 172
        x_to_add = 131
        start_y = 274
        y_to_add = 78
        size = (12, 15)
        records = load_records()
        for i, record in enumerate(records.values()):
            curr_x = start_x + i * x_to_add
            for j, time in enumerate(record.values()):
                curr_y = start_y + j * y_to_add
                display_time(self.screen, time, curr_x, curr_y, size)

    def run_main_menu(self):
        pygame.display.set_caption('Minesweeper menu')
        choice = self.menu_loop(MAIN_MENU_BUTTONS)
        if choice == 1:
            self.run_dimension_choice_menu()
        if choice == 2:
            self.run_rules()
        if choice == 3:
            self.run_high_scores()
        if choice == 4:
            self.flag = False
        pygame.quit()

    # Displays ending screen buttons on the screen
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

    # Checks if the mouse collides with any button and displays ending screen window on the screen
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

    # Runs the ending screen after the player finishes game
    def run_ending_screen(self, result, time, dimension_choice, difficulty):
        pygame.init()
        pygame.display.set_caption("Ending screen")
        self.screen = pygame.display.set_mode(MENU_SIZE)

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
