#!/usr/bin/env python3
from typing import Optional


def foo(x, y, z):
    bar(x)
    bar(y)
    bar(z)


def bar(x):
    print(f'enter bar{x}')
    baz(x)
    print(f'exit bar{x}')


def baz(x):
    print(int(x))


foo('123', '123x', '123')
