d = dict(a=10, b= 20, c=30)
values = d.values()
print(values)
print(len(values))
print(list(values))
print(reversed(values))
d['z'] = 99
print(values)
"""We can’t use [] to get individual items from a view"""
