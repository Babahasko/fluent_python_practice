print('=='*20)
print('Tuples as records')
lax_coordinates = (33.9425, -180.986)
city, year, populations, area = ('Tokyo', 2003, 32_450, 8014)
travel_ids = [('USA', '3185678'), ('BRA', '11894576'), ('ESP', '4482678')]
for passport in sorted(travel_ids):   # The % formatting operator understands tuples and treats
    print('%s%s' % passport)   # each item as a separate field

for country, _ in travel_ids:  # The for loop knows how to retrieve the items of a tuple separately—this is called
    print(country)  # “unpacking.” Here we are not interested in the second item, so we assign it to _, a
print(populations)  # dummy variable.

print('=='*20)
print('Tuples as Immutable Lists')

a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
print(a == b)
b[-1].append(99)
print(a == b)
'''Tuples with mutable items can be a source of bugs. An object is only hashable
if its value cannot ever change. An unhashable tuple cannot be inserted as a dict key,
or a set element.'''


def fixed(t):
    """ Function that shows if tuple has fixed values
    or not"""
    try:
        hash(t)
    except TypeError:
        return False
    return True


print(fixed(a))

print('=='*20)
print('Unpacking Sequence and Iterables')
print('parrallel assignment')
lax_coordinates = (33.592034, 78.123893)
lat, lon = lax_coordinates
print(lat)
print(lon)
print('swaping')
lat, lon = lon, lat
print(lat)
print(lon)

print('=='*20)
print('Using * to Grab Excess Items')
a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)  # * prefix can append in any position
a, *body, b, c = range(6)
print(a, body, b, c)

print('=='*20)
print('Unpacking with * in Function Calls and Sequence Literals')
# In function calls, we can use * multiple times:


def fun(a, b, c, d, *rest):
    return a, b, c, d, rest


result = fun(*[1, 2], 3, *range(4,  7))
print(result)

tupl = *range(4), 4
listik = [*range(4), 4]
obj = {*range(4), 4, *(5, 6, 7)}
print(tupl)
print(listik)
print('type = ', type(obj), obj)

print('=='*20)
print('Nested Unpacking')
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


def main():
    print(f'{"":15} | {"latitude":>9} | {"longtitude":>9}')
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


main()

print('=='*20)
print("Pattern Matching with Sequences")


class InvalidCommand(Exception):
    pass

# Example of match case


def handle_command(self, message):
    match message:
        case ['BEEPER', frequency, times]:  # This pattern matches any subject that is a sequence with three items.
           self.beep(times, frequency)  # The first item must be the string 'BEEPER'. The second and third item
        case ['NECK', angle]:  # can be anything, and they will be bound to the variables frequency and times,
           self.rotate_neck(angle) # in that order.
        case ['LED', ident, intensity]:  # This matches any subject with two items, the first being 'NECK'.
           self.leds[ident].set_brightness(ident, intensity)
        case ['LED', ident, red, green, blue]:
           self.leds[ident].set_color(ident, red, green, blue)
        case _:
           raise InvalidCommand(message)

metro_areas = [
 ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
 ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
 ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
 ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
 ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15}, {"latitude":>9}, {"longtitude":>9}')
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:15}, {lat:9.4f}, {lon:9.4f}')

main()

"""In general, a sequence pattern matches the subject if:
1. The subject is a sequence and;
2. The subject and the pattern have the same number of items and;
3. Each corresponding item matches, including nested items."""

#page 73