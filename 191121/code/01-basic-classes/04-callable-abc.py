#!/usr/bin/env python
from collections.abc import Callable


class Adder(Callable):
    def __init__(self, a: int) -> None:
        self.a = a

    def __call__(self, b: int) -> None:
        print(f'a + b = {self.a + b}')


x = Adder(3)
x(4)
