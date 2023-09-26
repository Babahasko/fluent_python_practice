l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
print(set(l))
print(list(set(l)))
print(dict.fromkeys(l).keys())
"""Count occurrences of needles in a haystack, both of type set 
found = len(needles & haystack)
it is better,
than found = 0
    for n in needles:
        if n in haystack:
            found += 1
"""
"""found = len(set(needles) & set(haystack))
# another way:
found = len(set(needles).intersection(haystack))"""
s = {1, 2, 3}
print(type(s))

print('=='*20)
print('Set Comprehensions')
from unicodedata import name
print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})

print('=='*20)
print('Set Operations on dict Views')
d1 = dict(a=1, b=2, c=3, d=4)
d2 = dict(b=20, d=40, e=50)
print(d1.keys() & d2.keys())
'''Note that the return value of & is a set. Even better: the set operators in dictionary
views are compatible with set instances. Check this out:'''
s = {'a', 'e', 'i'}
print(d1.keys() & s)
print(d1.keys() | s)

