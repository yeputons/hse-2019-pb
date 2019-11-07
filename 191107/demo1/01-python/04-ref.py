#!/usr/bin/env python3
a = 100
b = 200
print(a == b, a is b)
b = b / 2
print(a == b, a is b)
b = a
print(a == b, a is b)

print(None is None)
