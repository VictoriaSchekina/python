a = set([1, 2, 3, 5, 7])
b = set([2, 4, 6, 7, 8])
c = set([1, 2, 5, 6, 8])
print(a | b)
print(a & b)
print(a - b)
print(b - a)
print(a ^ b)
print()
print(' ')
print(a | c)
print(a & c)
print(a - c)
print(c - a)
print(a ^ c)
print(' ')
print(b | c)
print(b & c)
print(b - c)
print(c - b)
print(b ^ c)
print(' ')
number = (int(input('Enter a number')))
if number in a:
    print('The element is in set A')
else:
    print('The element is not in set A')




