#!/usr/bin/env python3

"""The solver file. It is going to solve all the problems, display expressions and exceptions."""

import sympy as sp
from rich.console import Console
from sympy import cos, cot, log, sin, tan
from sympy.parsing.sympy_parser import parse_expr

from vocabulary import *

cls = Console()


class Solver:
    x, y, z = sp.symbols("x y z")
    local_dict = {"x": x, "y": y, "z": z, "log": log, "ln": log}
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

            # if any(
            #     i in self.alphabet.lower() for i in str(self.user_expression.lower())
            # ):
            #     cls.print(f"[bold red]You must use only (x, y, z) variables![/]")
            #     quit()

            return self.expr

        except Exception as e:  # if there's a error
            raise ValueError(f"Parsing error: {self.user_expression}\n{e}")

    def solving(self):
        parsed = self.expr
        pretty_parsed_expr = sp.pretty(parsed)

        cls.print(f"[bold purple]Expression:\n{pretty_parsed_expr}[/]")

        if isinstance(
            parsed, sp.core.relational.Relational
        ):  # checks if there's Eq or Ineq and so on
            if isinstance(parsed, sp.Eq):  # if there's an equation
                solve_eq = sp.solveset(parsed)  # solves user's equation
                pretty_solved_eq = sp.pretty(solve_eq)  # pretty output
                cls.print(f"{OUTPUT_SOLUTION}[bold green]{pretty_solved_eq}[/]")

            else:
                solve_ineq = sp.solve_univariate_inequality(
                    parsed, self.x, domain=sp.S.Reals, relational=False
                )
                pretty_solved_ineq = sp.pretty(solve_ineq)
                cls.print(f"{OUTPUT_SOLUTION}[bold green]{pretty_solved_ineq}[/]")
