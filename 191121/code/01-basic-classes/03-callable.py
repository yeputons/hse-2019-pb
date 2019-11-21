#!/usr/bin/env python

class Adder:
    def __init__(self, a: int) -> None:
        self.a = a

    def __call__(self, b: int) -> int:
        return a + b


x = Adder(3)
y = Adder(10)
print(x(4))
print(y(4))
