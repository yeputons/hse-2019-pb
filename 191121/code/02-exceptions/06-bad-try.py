#!/usr/bin/env python3
from typing import Optional


def foo(x: str) -> None:
    try:
        bar(int(x))
        print('Ok')
    except ValueError:
        print(f'Invalid int: {x}')


def bar(x: int) -> None:
    if x != 10:
        raise ValueError(f'x should be 10')


foo('10')
foo('xxx')
foo('11')
