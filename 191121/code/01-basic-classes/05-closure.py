#!/usr/bin/env python3
def create_adder(a):
    def impl(b):
        print(f'a + b = {a + b}')
    return impl


x = create_adder(3)
x(4)
