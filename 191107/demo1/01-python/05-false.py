#!/usr/bin/env python3
print('Yes' if 2 == 2 else 'No')
print('Yes' if 0 else 'No')
print('Yes' if 1 else 'No')
print('Yes' if 0.5 else 'No')
print('Yes' if 0 else 'No')
print('Yes' if 'no' else 'No')
print('Yes' if '' else 'No')
print('Yes' if -1 else 'No')
print('Yes' if [1, 2, 3] else 'No')
print('Yes' if [False] else 'No')
print('Yes' if [] else 'No')

x = [1, 2, 3]
if len(x) > 0:
    print(x[0])
if x:
    print(x[0])

x and y == x if x else y
x or y == y if x else x

a = a or 'default'









