class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    def __get__(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

if __name__ == "__main__":
    d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    print(d['2'])
    print(d[4])
    print(d.get(1, 'N/A'))
    print(2 in d)
    print(1 in d)

"""A search like k in my_dict.keys() is efficient in Python 3 even for very large map‐
pings because dict.keys() returns a view, which is similar to a set, as we’ll see in
“Set Operations on dict Views” on page 110. However, remember that k in my_dict
does the same job, and is faster because it avoids the attribute lookup to find
the .keys method"""

