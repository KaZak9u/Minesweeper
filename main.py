from menu import Menu


def main():
    flag = True
    while flag:
        menu = Menu(flag)
        menu.run_main_menu()
        flag = menu.flag


if __name__ == "__main__":
    main()
