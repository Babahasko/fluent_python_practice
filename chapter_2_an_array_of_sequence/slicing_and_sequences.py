from array import array
from random import random
import numpy as np
from collections import deque

print('=='*20)
print('Slice Objects')
s = 'bycicle'
print(s[::3])
print(s[::-1])
print(s[::-2])

invoice = """
0.....6.................................40........52...55........
1909        Pimoroni PiBrella              $17.50   3     $52.50
1489        6mm Tactile Switch x20         $4.95    2     $9.90
1510        Panavise Jr. - PV-201          $28.00   1     $28.00
1601        PiTFT Mini Kit 320x240         $34.95   1     $34.95
"""
SKU = slice(0,6)
DESCRIPTION = slice(6,40)
UNIT_PRICE = slice(40,52)
QUANTITY = slice(52,55)
ITEM_TOTAL = slice(55,None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

print('=='*20)
print('Assigning to Slices')
l = list(range(20))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::7] = [11, 12]
print(l)
l[2:5] = [100]  # When the target of the assignment is a slice, the righthand side must be an
print(l)        # iterable object, even if it has just one item.

print('=='*20)
print('Using + and * with Sequences')
l = [1, 2, 3]
print(l * 5)
print(5 * 'abcd')

print('=='*20)
print('Building Lists of Lists')

board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2] = 'X'
print(board)
print('Wierd board')
wierd_board = [['_'] * 3] * 3  # useless list
wierd_board[1][2] = 'X'
print(wierd_board)

print('=='*20)
print('Augmented Assignment with Sequences')
print('demonstration of *= with a mutable sequence and then an immutable one')
l = [1, 2, 3]
print(id(l))
l *= 2
print(l)
print(id(l))
l = (1, 2, 3)
print(id(l))
l *= 2
print(l)
print(id(l))

print('=='*20)
print('list.sort Versus the sorted Built-In')
"""The list.sort method sorts a list in place—that is, without making a copy. It returns
None to remind us that it changes the receiver and does not create a new list. In contrast,
the built-in function sorted creates a new list and returns it."""
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(fruits)
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
print(fruits)
fruits.sort()
print(fruits)

print('=='*20)
print('Arrays')
'''If a list only contains numbers, an array.
array is a more efficient replacement.'''
"""A Python array is as lean as a C array. As shown in Figure 2-1, an array of float
values does not hold full-fledged float instances, but only the packed bytes repre‐
senting their machine values—similar to an array of double in the C language. When
creating an array, you provide a typecode, a letter to determine the underlying C
type used to store each item in the array. For example, b is the typecode for what
C calls a signed char, an integer ranging from –128 to 127. If you create an
array('b'), then each item will be stored in a single byte and interpreted as an inte‐
ger. For large sequences of numbers, this saves a lot of memory. And Python will not
let you put any number that does not match the type for the array."""

# floats = array('d', (random() for i in range(10**7)))
# print(floats[-1])
# with open('floats.bin', 'wb') as f:
#     floats.tofile(f)
# floats2 = array('d')
# with open('floats.bin', 'rb') as f:
#     floats2.fromfile(f, 10**7)
# print(floats2[-1])
# print(floats2 == floats)

print('=='*20)
print('Memory Views')
"""A memoryview is essentially a generalized NumPy array structure in Python itself
(without the math). It allows you to share memory between data-structures (things like
PIL images, SQLite databases, NumPy arrays, etc.) without first copying. This is very
important for large data sets."""

octets = array('B', range(6))
print(octets)
m1 = memoryview(octets)
print(m1.tolist())
m2 = m1.cast('B', [2,3])
print(m2.tolist())
m3 = m1.cast('B',[3, 2])
print(m3.tolist())
m2[1, 1] = 22
m3[1, 1] = 33
print(octets)

print('=='*20)
print('NumPy')
a = np.arange(12)
print(a)
print(type(a))
print(a.shape)
a.shape = 3,4
print(a)
print(a[2])
print(a[2,1])
print(a[:,1])
print(a.transpose())

print('=='*20)
print('Deques and Other Queues')
'''The .append and .pop methods make a list usable as a stack or a queue (if you
use .append and .pop(0), you get FIFO behavior). But inserting and removing from
the head of a list (the 0-index end) is costly because the entire list must be shifted in
memory'''

dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
print(dq)
dq.extend([11, 22, 33])
print(dq)
dq.extendleft([10, 20, 30, 40])
print(dq)

"""Python sequences are often categorized as mutable or immutable, but it is also useful
to consider a different axis: flat sequences and container sequences. The former are
more compact, faster, and easier to use, but are limited to storing atomic data such as
numbers, characters, and bytes. Container sequences are more flexible, but may sur‐
prise you when they hold mutable objects, so you need to be careful to use them cor‐
rectly with nested data structures.
Unfortunately, Python has no foolproof immutable container sequence type: even
“immutable” tuples can have their values changed when they contain mutable items
like lists or user-defined objects.
List comprehensions and generator expressions are powerful notations to build and
initialize sequences. If you are not yet comfortable with them, take the time to master
their basic usage. It is not hard, and soon you will be hooked.
Tuples in Python play two roles: as records with unnamed fields and as immutable
lists. When using a tuple as an immutable list, remember that a tuple value is only
guaranteed to be fixed if all the items in it are also immutable. Calling hash(t) on a
tuple is a quick way to assert that its value is fixed. A TypeError will be raised if t
contains mutable items.
When a tuple is used as a record, tuple unpacking is the safest, most readable way of
extracting the fields of the tuple. Beyond tuples, * works with lists and iterables in
many contexts, and some of its use cases appeared in Python 3.5 with PEP 448—
Additional Unpacking Generalizations. Python 3.10 introduced pattern matching
with match/case, supporting more powerful unpacking, known as destructuring.
Sequence slicing is a favorite Python syntax feature, and it is even more powerful
than many realize. Multidimensional slicing and ellipsis (...) notation, as used in
NumPy, may also be supported by user-defined sequences. Assigning to slices is a
very expressive way of editing mutable sequences.
Repeated concatenation as in seq * n is convenient and, with care, can be used to
initialize lists of lists containing immutable items. Augmented assignment with +=
and *= behaves differently for mutable and immutable sequences. In the latter case,
these operators necessarily build new sequences. But if the target sequence is
70 | Chapter 2: An Array of Sequences
mutable, it is usually changed in place—but not always, depending on how the
sequence is implemented.
The sort method and the sorted built-in function are easy to use and flexible, thanks
to the optional key argument: a function to calculate the ordering criterion. By the
way, key can also be used with the min and max built-in functions.
Beyond lists and tuples, the Python standard library provides array.array. Although
NumPy and SciPy are not part of the standard library, if you do any kind of numeri‐
cal processing on large sets of data, studying even a small part of these libraries can
take you a long way."""

