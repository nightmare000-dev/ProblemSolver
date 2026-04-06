#!/usr/bin/env python3

"""The derivative page. Will find derivatives of anything"""

import sympy as sp
from rich.console import Console
from sympy import cos, cot, log, sin, tan
from sympy.parsing.sympy_parser import parse_expr

from vocabulary import *

cls = Console()


class Derivative:
    x, y, z = sp.symbols("x y z")
    local_dict = {
        "x": x,
        "y": y,
        "z": z,
        "log": log,
        "ln": log,
        "cos": cos,
        "sin": sin,
        "tan": tan,
        "cot": cot,
    }
    alphabet = "QWERTUIOPASDFGHJKLCVBNM"

    def get_users_expression(self):  # invites
        self.user_expression = cls.input(INVITATIONS[1])

    def parse_user_expr(self):
        try:  # tries to parse user's expression
            self.expr = parse_expr(
                self.user_expression,
                local_dict=self.local_dict,
                transformations="all",
                evaluate=False,
            )
            return self.expr

        except Exception as e:  # if there's a error
            raise ValueError(f"Parsing error: {self.user_expression}\n{e}")

    def find_derivative(self):
        parsed = self.expr
        pretty_parsed_expr = sp.pretty(parsed)  # makes the expression pretty for visual

        cls.print(f"[bold purple]Expression:\n{pretty_parsed_expr}[/]")

        diff = sp.diff(parsed)  # finds a derivative
        pretty_diff = sp.pretty(diff)  # makes it pretty
        cls.print(f"{OUTPUT_SOLUTION}[bold green]{pretty_diff}[/]")
