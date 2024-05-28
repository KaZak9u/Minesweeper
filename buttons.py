import pygame

""" BUTTON LOCATIONS """

BUTTON_1_LOCATION = (150, 200)
BUTTON_2_LOCATION = (150, 300)
BUTTON_3_LOCATION = (150, 400)
BUTTON_4_LOCATION = (275, 500)

""" MAIN MENU BUTTONS """

BUTTON_PLAY_IMAGE = pygame.image.load("Assets/button_play.png")
BUTTON_PLAY_CHOSEN_IMAGE = pygame.image.load("Assets/button_chosen_play.png")
BUTTON_1_RECT = BUTTON_PLAY_IMAGE.get_rect()
BUTTON_1_RECT.topleft = BUTTON_1_LOCATION

BUTTON_RULES_IMAGE = pygame.image.load("Assets/button_rules.png")
BUTTON_RULES_CHOSEN_IMAGE = pygame.image.load("Assets/button_chosen_rules.png")
BUTTON_2_RECT = BUTTON_RULES_IMAGE.get_rect()
BUTTON_2_RECT.topleft = BUTTON_2_LOCATION

BUTTON_HIGH_SCORES_IMAGE = pygame.image.load("Assets/button_high_scores.png")
BUTTON_HIGH_SCORES_CHOSEN_IMAGE = pygame.image.load("Assets/button_chosen_high_scores.png")
BUTTON_3_RECT = BUTTON_HIGH_SCORES_IMAGE.get_rect()
BUTTON_3_RECT.topleft = BUTTON_3_LOCATION

BUTTON_EXIT_IMAGE = pygame.image.load("Assets/button_exit.png")
BUTTON_EXIT_CHOSEN_IMAGE = pygame.image.load("Assets/button_exit_chosen.png")
BUTTON_4_RECT = BUTTON_EXIT_IMAGE.get_rect()
BUTTON_4_RECT.topleft = BUTTON_4_LOCATION

MAIN_MENU_BUTTONS = [BUTTON_PLAY_CHOSEN_IMAGE, BUTTON_PLAY_IMAGE, BUTTON_RULES_CHOSEN_IMAGE, BUTTON_RULES_IMAGE,
                     BUTTON_HIGH_SCORES_CHOSEN_IMAGE, BUTTON_HIGH_SCORES_IMAGE, BUTTON_EXIT_CHOSEN_IMAGE, BUTTON_EXIT_IMAGE]
BUTTON_RECTS = [BUTTON_1_RECT, BUTTON_2_RECT, BUTTON_3_RECT, BUTTON_4_RECT]

""" DIMENSION CHOICE BUTTONS """

BUTTON_10x10_IMAGE = pygame.image.load("Assets/button_10x10.png")
BUTTON_10x10_CHOSEN_IMAGE = pygame.image.load("Assets/button_10x10_chosen.png")

BUTTON_14x14_IMAGE = pygame.image.load("Assets/button_14x14.png")
BUTTON_14x14_CHOSEN_IMAGE = pygame.image.load("Assets/button_14x14_chosen.png")

BUTTON_24x16_IMAGE = pygame.image.load("Assets/button_24x16.png")
BUTTON_24x16_CHOSEN_IMAGE = pygame.image.load("Assets/button_24x16_chosen.png")

BUTTON_BACK_IMAGE = pygame.image.load("Assets/button_back.png")
BUTTON_BACK_CHOSEN_IMAGE = pygame.image.load("Assets/button_back_chosen.png")

DIMENSION_CHOICE_BUTTONS = [BUTTON_10x10_CHOSEN_IMAGE, BUTTON_10x10_IMAGE, BUTTON_14x14_CHOSEN_IMAGE, BUTTON_14x14_IMAGE,
                            BUTTON_24x16_CHOSEN_IMAGE, BUTTON_24x16_IMAGE, BUTTON_BACK_CHOSEN_IMAGE, BUTTON_BACK_IMAGE]

""" DIFFICULTY CHOICE BUTTONS """

BUTTON_EASY_IMAGE = pygame.image.load("Assets/button_easy.png")
BUTTON_EASY_CHOSEN_IMAGE = pygame.image.load("Assets/button_easy_chosen.png")

BUTTON_MEDIUM_IMAGE = pygame.image.load("Assets/button_medium.png")
BUTTON_MEDIUM_CHOSEN_IMAGE = pygame.image.load("Assets/button_medium_chosen.png")

BUTTON_HARD_IMAGE = pygame.image.load("Assets/button_hard.png")
BUTTON_HARD_CHOSEN_IMAGE = pygame.image.load("Assets/button_hard_chosen.png")

DIFFICULTY_CHOICE_BUTTONS = [BUTTON_EASY_CHOSEN_IMAGE, BUTTON_EASY_IMAGE, BUTTON_MEDIUM_CHOSEN_IMAGE,
                             BUTTON_MEDIUM_IMAGE, BUTTON_HARD_CHOSEN_IMAGE, BUTTON_HARD_IMAGE, BUTTON_BACK_CHOSEN_IMAGE,
                             BUTTON_BACK_IMAGE]