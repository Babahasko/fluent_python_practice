from collections import OrderedDict


print('=='*20)
print('Dict Comprehensions')
dial_codes = [(880, 'Bangladesh'),
              (55, 'Brazil'),
              (86, 'China'),
              (91, 'India'),
              (62, 'Indonesia'),
              (81, 'Japan'),
              (234, 'Nigeria'),
              (92, 'Pakistan'),
              (7, 'Russia'),
              (1, 'United States'),
              ]
country_dial = {country: code for code, country in dial_codes}
print(country_dial)
country_dial_2 = {code: country.upper()
                  for country, code in sorted(country_dial.items())
                  if code < 70}
print(country_dial_2)

print('=='*20)
print('Unpacking Mappings')

def dump(**kwargs):
    return kwargs

result = dump(**{'x':1}, y=2, **{'z':3})
print(result)

print({'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}})
"""In this case, duplicate keys are allowed. Later occurrences overwrite previous ones—
see the value mapped to x in the example."""

print('=='*20)
print('Merging Mappings with |')
d1= {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
print(d1|d2)

print('using |= syntax')
"""To update an existing mapping in place, use |="""
print(d1)
d1 |= d2
print(d1)

print('=='*20)
print('Pattern Matching with Mappings')
def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api':2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': book}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'invalid record: {record!r}')
b1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Gödel, Escher, Bach')
author = get_creators(b1)
print(author)
b2 = OrderedDict(api=2, type='book', title='Python in Nutshell',
                 authors='Martelli Ravenscroft Holden'.split())
author = get_creators(b2)
print(author)
#author = get_creators({'type': 'book', 'pages': 770})
#print(author)
# author = get_creators('Spam, spam, spAAAMMM!')
# print(author)

"""In contrast with sequence patterns, mapping patterns succeed on partial matches. In
the doctests, the b1 and b2 subjects include a 'title' key that does not appear in any
'book' pattern, yet they match.
There is no need to use **extra to match extra key-value pairs, but if you want to
capture them as a dict, you can prefix one variable with **. It must be the last in the
pattern, and **_ is forbidden because it would be redundant. A simple example:"""

food = dict(category='ice cream', flavor='vanilla', cost=199)
match food:
    case {'category': 'ice cream', **details}:
        print(f'Ice cream details: {details}')
