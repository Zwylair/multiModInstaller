import os
from types import ModuleType
from typing import Dict, Callable
try:
    import msvcrt
except ImportError:
    input('Your system is not supported yet to use this script.\n\nPress ENTER to exit.')
    exit(1)


class MenuParent:
    """ Used to make possible append Menu class to items annotation """
    pass


class Menu(MenuParent):
    def __init__(self, name: str, items: Dict[ModuleType, Callable | MenuParent] | None = None):
        self.name = name
        self.items = items
        self._back_to_menu: Menu | None = None

    @staticmethod
    def _cls():
        os.system('cls')

    def _print_menu(self):
        self._cls()

        menu_template = '\t[{0}] -- open {1} menu'
        func_template = '\t[{0}] -- install {1} mod'
        exit_template = '\t[0] -- exit'
        back_template = '\t[0] -- back to previous menu'

        print(f'{self.name} menu:')
        print(exit_template if self._back_to_menu is None else back_template)

        for index, menu_item in enumerate(self.items.items()):
            template = menu_template if isinstance(menu_item[1], Menu) else func_template
            print(template.format(index + 1, menu_item[0].__name__.split('.')[-1]))

        print('\n')

    def back_to_previous_menu(self):
        if isinstance(self._back_to_menu, Menu):
            self._back_to_menu.run()
        elif self._back_to_menu is None:
            exit(0)

    def run(self):
        while True:
            menu_items = {0: self.back_to_previous_menu}
            menu_items |= {index + 1: module for index, module in enumerate(self.items.values())}

            self._print_menu()

            while True:
                try:
                    got_input = int(msvcrt.getch().decode('utf-8'))
                except ValueError:
                    continue

                if got_input in menu_items.keys():
                    callable_item = menu_items[got_input]

                    if isinstance(callable_item, Menu):
                        callable_item._back_to_menu = self
                        callable_item.run()
                    elif isinstance(callable_item, Callable):
                        callable_item()

                        print('\nPress any key to back to menu.')
                        msvcrt.getch()
                    break
