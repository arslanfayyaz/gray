class CustomDict(dict):
    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def update(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise TypeError("update expected at most 1 arguments, got %d" % len(args))

            other = dict(args[0])

            for key in other:
                self[key] = other[key]

    def __setitem__(self, key, value):
        if not isinstance(key, (str, int)):
            raise TypeError('key must be a string or an integer')

        if not isinstance(value, str):
            raise TypeError('value must be a string')

        dict.__setitem__(self, key, value)

    def __getitem__(self, key):
        if key not in self:
            raise KeyError('key not found: %s' % key)

        return dict.__getitem__(self, key)

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('key must be an integer')

        dict.__delitem__(self, key)

    def keys(self):
        return dict.keys(self)

    def values(self):
        return dict.values(self)

    def pop(self, key, default=None):
        if not isinstance(key, (str, int)):
            raise TypeError('key must be a string or an integer')

        if key not in self:
            if default is not None:
                return default

            raise KeyError('key not found: %s' % key)

        value = self[key]
        del self[key]
        return value

    def clear(self):
        super().clear()

    def copy(self):
        return CustomDict(self)

    def setdefault(self, key, default=None):
        if key not in self:
            self[key] = default

        return self[key]

    def pullrequest(self):
        print("hello this is pull request")


custom_dict = CustomDict({'key1': 'value1', 'key2': 'value2'})
print(custom_dict)

custom_dict["key3"] = "arsh"
custom_dict["key4"] = "mom"

print(custom_dict)

copy_dict = custom_dict.copy()

custom_dict.clear()

print(custom_dict)
print(copy_dict)

value = custom_dict.setdefault('key2', 'new_value')
print(value)
print(custom_dict)
