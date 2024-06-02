import pygame

IMG_0 = pygame.image.load("Assets/time_display/0.png")
IMG_1 = pygame.image.load("Assets/time_display/1.png")
IMG_2 = pygame.image.load("Assets/time_display/2.png")
IMG_3 = pygame.image.load("Assets/time_display/3.png")
IMG_4 = pygame.image.load("Assets/time_display/4.png")
IMG_5 = pygame.image.load("Assets/time_display/5.png")
IMG_6 = pygame.image.load("Assets/time_display/6.png")
IMG_7 = pygame.image.load("Assets/time_display/7.png")
IMG_8 = pygame.image.load("Assets/time_display/8.png")
IMG_9 = pygame.image.load("Assets/time_display/9.png")
IMG_COLON = pygame.image.load("Assets/time_display/colon.png")

CHAR_TO_IMAGE_DICT = {
    '0': IMG_0, '1': IMG_1, '2': IMG_2, '3': IMG_3, '4': IMG_4, '5': IMG_5, '6': IMG_6, '7': IMG_7, '8': IMG_8,
    '9': IMG_9, ':': IMG_COLON
}


def display_time(screen, time_str, x, y, size):
    for index, char in enumerate(time_str):
        screen.blit(pygame.transform.scale(CHAR_TO_IMAGE_DICT[char], size), (x + index * size[1], y))