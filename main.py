#!/usr/bin/env python3

"""The project's main file. Displays a page with 2 options: (solver and helper).
User can choose one of these options and it will be redirected after choosing"""

import os

from pyfiglet import Figlet
from rich.console import Console

from functions import Functions
from options import Options
from pages.derivativePage import Derivative
from pages.helperPage import Helper
from pages.solver import Solver
from vocabulary import *

os.system("cls")

fgl = Figlet(font="slant", justify="center")  # initialization Figlet
cls = Console()  # initialization rich.console

opt_obj = Options()  # for options
func_obj = Functions()  # for functions
solver_obj = Solver()  # for running Solver's methods
helper_obj = Helper()  # for Helper's methods
derivate_obj = Derivative()  # for Derivatieves methods


class Menu:
    def menu_page(self):
        title_text = fgl.renderText(TITLES[0])
        print(title_text)  # displays title text

        opt_obj.title_display()  # displays options
        choose_option_inv = cls.input(INVITATIONS[0])  # invitation

        if choose_option_inv in ["1", "2", "3", "4"]:
            if choose_option_inv == "1":
                func_obj.open_solver()  # clears terminal, redirects to the Solver page
                solver_obj.get_users_expression()  # invitation for user to input its expression
                solver_obj.parse_user_expr()  # parses user's expression
                solver_obj.solving()
            elif choose_option_inv == "2":
                func_obj.open_helper()  # clears terminal, redirects to the Helper page
                helper_obj.output_help()
            elif choose_option_inv == "3":
                func_obj.open_derivative()  # clears terminal, redirects to the Derivative page
                derivate_obj.get_users_expression()  # invitation for user to input its expression
                derivate_obj.parse_user_expr()  # parses user's expression
                derivate_obj.find_derivative()  # finds derivative
            elif choose_option_inv == "4":  # finishes the session
                quit()
        else:
            cls.print(OPTION_ERROR)  # displays ERROR


if __name__ == "__main__":
    while True:
        menu_obj = Menu()
        menu_obj.menu_page()
        cls.input(ENDING)
        os.system("cls")
