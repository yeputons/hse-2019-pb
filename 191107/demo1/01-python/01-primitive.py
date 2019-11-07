#!/usr/bin/env python3
i = 0
i += 1
print('Hello World')
print(i)
print('Hello,', i)

for i in range(10):
    print('1: i=', i)

for i in range(10, 0, -2):
    print('2: i=', i)

a = 0
b = 1
while a < 100:
    ab = a + b
    a = b
    b = ab
print(b)

if b % 2 == 0 and 2 * 2 == 4:
    print('Even')
else:
    print('Odd')

print('Even' if b % 2 == 0 else 'Odd')
print(b / 100)
print(b // 100)
print(2.3 % 1.3)



