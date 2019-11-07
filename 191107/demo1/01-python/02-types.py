#!/usr/bin/env python3
print(0 + 0)
print('0' + '0')
# print(0 + '0')
print(type(0))
print(type('0'))

print(ord('c') - ord('a'))
print(int('20') - int('10'))

print('Hello, ' + str(123))
print('Hello, ' + hex(123))
print('Hello, ' + bin(123))

print(('a' == 'a') + 10)

do_something = input('Do something? ') == 'yes'
print(do_something)
x = 'foo' if do_something else 100
print(type(x))
print(str(x) + 'bar')
x = [1, 2, 3]
print(x)

print(f'2 + 2 = {2 + 2}')
x = 2 + 2
print(f'2 + 2 = {x} yes!')
