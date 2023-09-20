import array

print('=='*20)
print('Example of list_comp')
symbols = 'A12u3SDl0-^$'
codes = [ord(i) for i in symbols]
print(codes)

print('=='*20)
print('Walrus operator')
x = 'ABC'
codes = [laster := ord(c) for c in x]
print(laster)
print(codes)

print('=='*20)
print('The same list built by a listcomp and a map/filter composition')
symbols = '!(*@$&)('
numbers_asi = [ord(c) for c in symbols if ord(c) < 127]
print(numbers_asi)
numbers_map_filter = list(filter(lambda c: c < 127, map(ord, symbols)))
print(numbers_map_filter)

print('=='*20)
print('Example of Cartesian Product')
colors = ['red', 'blue', 'white']
cars = ['toyota', 'hyndai', 'skoda']
list_of_cars = [(color, car) for color in colors for car in cars]
print(list_of_cars)

print('=='*20)
print('Initializing a tuple and an array from a generator expression')
symbols = '"!@)($)'
tup_seq = tuple(ord(c) for c in symbols)
print(tup_seq)

arr_seq = array.array('I', (ord(s) for s in symbols))
print(arr_seq)


