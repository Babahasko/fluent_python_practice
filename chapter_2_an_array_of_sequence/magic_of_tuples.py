print('=='*20)
print('Tuples as records')
lax_coordinates = (33.9425, -180.986)
city, year, populations, area = ('Tokyo', 2003, 32_450, 8014)
travel_ids = [('USA', '3185678'), ('BRA', '11894576'), ('ESP', '4482678')]
for passport in sorted(travel_ids): #The % formatting operator understands tuples and treats
    print('%s%s' % passport) # each item as a separate field

for country, _ in travel_ids: #The for loop knows how to retrieve the items of a tuple separately—this is called
    print(country) #“unpacking.” Here we are not interested in the second item, so we assign it to _, a
print(populations) # dummy variable.

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
    ''' Function that shows if tuple has fixed values
    or not'''
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
lat,lon = lon, lat
print(lat)
print(lon)
#page 66