#!/usr/bin/env python3

"""The vocabulary file is going to keep here
all the words and phrases
for different things"""

from rich.console import Console

cls = Console()

TITLES: list = [
    "Problem solver",
    "Helper",
    "Solver",
    "Derivative",
]  # all the titles (Problem solver, Helper, Solver)
MENU: dict = {
    "[bold cyan](1)[/]": "[bold cyan] - Solver[/]",
    "[bold magenta](2)[/]": "[bold magenta] - Helper[/]",
    "[bold green](3)[/]": "[bold green] - Derivative[/]",
    "[bold red](4)[/]": "[bold red] - Exit[/]",
}  # for menu options
INVITATIONS: list = [
    "[bold italic red]\n$ [/]",
    "[bold cyan]Your expression: [/]",
]  # invitations for user
ENDING: str = "[bold italic red]\nPress ENTER to continue...[/]"  # if it is the end of the program
OPTION_ERROR: str = "[bold red]Error! Choose 1, 2 or 3 option![/]"  # if a user wrote anything other than 1 or 2
OUTPUT_SOLUTION: str = "[bold green]Here you go:\n[/]"
HELPER: str = """***

#
==================== HELP ====================

THE PROGRAM SOLVES:

    Equations

    Inequalities

HOW TO WRITE INPUT:

    EQUATIONS
    Example:
    x^2 - 4 = 0

    INEQUALITIES
    Examples:
    x^2 - 4 > 0
    x^2 - 4 >= 0
    x^2 - 4 < 0
    x^2 - 4 <= 0

    FRACTIONS
    Write them using a regular slash:
    1/2
    (x+1)/3
    x/(x-2)

    POWERS
    You can write them like this:
    x^2
    x**2
    (x+1)^3

    ROOTS
    Square root:
    sqrt(x)
    sqrt(x+1)

n-th root:
(x+1)^(1/3)

    LOGARITHMS
    log(x)
    log(x, 10)

    TRIGONOMETRY
    sin(x)
    cos(x)
    tan(x)

    BRACKETS
    Use regular round brackets:
    (x+1)^2
    (x-2)/(x+3)

    VARIABLE
    Usually the variable is x.
    If the program supports other variables, that will be mentioned separately.

IMPORTANT:

    Do not write text words like "fraction".

    Do not write "squared".

    Do not write "root" instead of sqrt if the program does not support it directly.

    If the input is incorrect, the program will show an error.

EXAMPLES:

    x^2 - 4 = 0

    x^2 - 4 > 0

    sin(x) = 1/2

    log(x) = 2

    sqrt(x) = 3

=============================================="""
