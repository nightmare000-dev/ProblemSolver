#!/usr/bin/env python3

"""This is a file for all the functions"""

import os

from pyfiglet import Figlet

from vocabulary import *

fgl = Figlet(font="slant")  # initialization Figlet


class Functions:
    @staticmethod
    def open_solver():  # directs to the Solver page and clears terminal
        os.system("clear")
        print(fgl.renderText(TITLES[2]))

    @staticmethod
    def open_helper():  # directs to the Helper page and clears terminal
        os.system("clear")
        print(fgl.renderText(TITLES[1]))

    @staticmethod
    def open_derivative():  # directs to the Derivative page and clears terminal
        os.system("clear")
        print(fgl.renderText(TITLES[3]))
