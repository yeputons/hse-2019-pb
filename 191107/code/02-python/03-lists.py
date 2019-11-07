#!/usr/bin/env python3
# Lists are heterogenous (rarely used)
a = [1, 2, 'foo', 'bar']
print(a)
print(a + [3, 4])
print(a[0])
a[0] = 3  # Mutable
print(a)

# Builtins
print(len([1, 2, 3]))
print(min([1, 2, 3]))
print(sum([1, 2, 3]))

# Slices
print(a[0:2])
print(a[0:4:2])
print(a[0::2])

# List modification
a.append(100)
print(a)

# List comprehension
print([x + 2 for x in range(10)])
print([x + 2 for x in range(10) if x % 2 == 0])

# Note that range is not a list, it's generator:
x = range(1, 10000000000)
print(x)
print(x[1:10])
print(list(x[1:10]))
for i in x:
    print(i)

# There are generator expressions
x = (x + 2 for x in range(10))
print(x)
print(list(x))
print(list(x))
print(x + 2 for x in range(10))  # Syntax sugar
print([x + 2 for x in range(10)])  # List comprehension
print(len(x + 2 for x in range(10)))  # Errror

# Strings
print('foo')
print([x for x in 'foo'])
print(list('foo'))  # https://docs.python.org/3/library/
