#!/usr/bin/env python3
a = [1, 2, 'foo', 'bar']
print(a)
print(a + [3, 4])
print(a[0])
a[0] = 3
print(a)
a[2] = [3, 4]
print(a)

print(len([1, 2, 3]))
print(min([1, 2, 3]))
print(sum([1, 2, 3]))

print(a[0:2])
print(a[0:4:2])
print(a[0::2])
print(a[::-1])
print(a[-3::-1])
print(a[-3:-1])

a.append(100)
print(a)

print([x + 2 for x in range(10)])
print([x + 2 for x in range(10) if x % 2 == 0])

x = range(1, 1000000000000000000000)
print(x)
print(x[1:10])
print(list(x[1:10]))

x = (x + 2 for x in range(10))
print(x)
print(list(x))
print(list(x))
print(x + 2 for x in range(10))
print([x + 2 for x in range(10)])
#print(len(x + 2 for x in range(10)))

print('foo')
print([x for x in 'foo'])
print(list('foo'))





