import pygame
from menu import Menu

pygame.font.init()


def main():
    menu = Menu()
    menu.run_main_menu()


if __name__ == "__main__":
    main()
