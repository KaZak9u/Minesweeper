from buttons import *

pygame.init()

BACKGROUND_IMAGE = pygame.image.load("Assets/menu_background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (600, 600))


class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for index, button in enumerate(BUTTON_RECTS):
                            if button.collidepoint(mouse_pos):
                                choice = index + 1
                                running = False
            self.clock.tick(60)
        return choice

    def run_dimension_choice_menu(self):
        pygame.display.set_caption('Select dimension')
        choice = self.menu_loop(DIMENSION_CHOICE_BUTTONS)
        if choice == 4:
            self.run_main_menu()
        pygame.quit()

    def run_main_menu(self):
        pygame.display.set_caption('Minesweeper menu')
        choice = self.menu_loop(MAIN_MENU_BUTTONS)
        if choice == 1:
            self.run_dimension_choice_menu()
        pygame.quit()


if __name__ == "__main__":
    menu = Menu()
    menu.run_main_menu()
