import pygame

BACKGROUND_IMAGE = pygame.image.load("Assets/menu_background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (600, 600))


class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 600))
