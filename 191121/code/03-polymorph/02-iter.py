#!/usr/bin/env python3
my_range = range(5, 10)

iterator = iter(my_range)
# iterator = my_range.__iter__() # Так не пишем, пишем iter()
print(iterator)

v0 = next(iterator)
# v0 = iterator.__next__() # Так не пишем, пишем next()
print(v0)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))  # StopIteration

print(my_range[5])  # IndexError
