import pygame

pygame.init()

BACKGROUND_IMAGE = pygame.image.load("Assets/menu_background.png")
BUTTON_PLAY_IMAGE = pygame.image.load("Assets/button_play.png")
BUTTON_PLAY_CHOSEN_IMAGE = pygame.image.load("Assets/button_chosen_play.png")
BUTTON_RULES_IMAGE = pygame.image.load("Assets/button_rules.png")
BUTTON_RULES_CHOSEN_IMAGE = pygame.image.load("Assets/button_chosen_rules.png")
BUTTON_HIGH_SCORES_IMAGE = pygame.image.load("Assets/button_high_scores.png")
BUTTON_HIGH_SCORES_CHOSEN_IMAGE = pygame.image.load("Assets/button_chosen_high_scores.png")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (600, 600))

PLAY_BUTTON_LOCATION = (150, 200)
RULES_BUTTON_LOCATION = (150, 300)
HIGH_SCORES_BUTTON_LOCATION = (150, 400)


class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 600))

    def draw_window(self, play_chosen, rules_chosen, high_scores_chosen):
        self.screen.blit(BACKGROUND, (0, 0))
        if play_chosen:
            self.screen.blit(BUTTON_PLAY_CHOSEN_IMAGE, PLAY_BUTTON_LOCATION)
        else:
            self.screen.blit(BUTTON_PLAY_IMAGE, PLAY_BUTTON_LOCATION)
        if rules_chosen:
            self.screen.blit(BUTTON_RULES_CHOSEN_IMAGE, RULES_BUTTON_LOCATION)
        else:
            self.screen.blit(BUTTON_RULES_IMAGE, RULES_BUTTON_LOCATION)
        if high_scores_chosen:
            self.screen.blit(BUTTON_HIGH_SCORES_CHOSEN_IMAGE, HIGH_SCORES_BUTTON_LOCATION)
        else:
            self.screen.blit(BUTTON_HIGH_SCORES_IMAGE, HIGH_SCORES_BUTTON_LOCATION)
        pygame.display.update()

    def run(self):
        running = True
        while running:
            self.draw_window(True, False, True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()


if __name__ == "__main__":
    menu = Menu()
    menu.run()