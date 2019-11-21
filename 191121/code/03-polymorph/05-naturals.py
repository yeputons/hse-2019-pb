#!/usr/bin/env python3
from collections.abc import Iterator
import itertools


class Naturals(Iterator):
    def __init__(self):
        self.value = 0

    #def __iter__(self):
    #    return self

    def __next__(self):
        self.value += 1
        return self.value


def print_first(it, remaining):
    for i in it:
        print(i)
        remaining -= 1
        if not remaining:
            break


it = Naturals()
#for i in it:
#    print(i)
print(type(it) == Iterator)
print(isinstance(it, Iterator))
print(list(itertools.islice(it, 3)))
print(itertools.islice(it, 10))
print(list(itertools.islice(it, 4)))
