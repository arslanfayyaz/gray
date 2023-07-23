class CustomDict(dict):
    def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        self.update(*args, **kwargs)

    def update(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise TypeError("update expected at most 1 arguments, got %d" % len(args))
            other = dict(args[0])
            for key in other:
                self[key] = other[key]

    def __setitem__(self, key, value):
        # Allow only string or integer as keys
        if not isinstance(key, (str, int)):
            raise TypeError('key must be a string or an integer')

        # Allow only string as values
        if not isinstance(value, str):
            raise TypeError('value must be a string')

        dict.__setitem__(self, key, value)

    def __getitem__(self, key):
        # Check if key exists
        if key not in self:
            raise KeyError('key not found: %s' % key)
        return dict.__getitem__(self, key)

    def __delitem__(self, key):
        # Allow only integers as keys, same as _setitem_ method
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
        # Remove all items from the dictionary
        super().clear()

    def copy(self):
        # Create a shallow copy of the dictionary
        return CustomDict(self)

    def setdefault(self, key, default=None):
        # Set the key to the default value if key is not in dictionary
        if key not in self:
            self[key] = default
        return self[key]

    def pullrequest(self):
        print("hello this is pull request")


# custom_dict = CustomDict({'key1': 'value1', 'key2': 'value2'})
#
# # Access the values
# print(custom_dict['key1'])  # Output: 'value1'
# print(custom_dict['key2'])  # Output: 'value2'
# d = CustomDict()
# print(d)
# d['x'] = 1  # OK
# d[1] = 1  # Raises TypeError: key must be a string
# d['x'] = 'y'  # Raises TypeError: value must be an integer
# print(d['x'])  # OK: prints 1
# print(d['y'])  # Raises KeyError: key not found: y

# d[1] = "arslan"
# d[2] = "ali"
# print(d[1])
# print(d[2])

custom_dict = CustomDict({'key1': 'value1', 'key2': 'value2'})
print(custom_dict)  # Output: {'key1': 'value1', 'key2': 'value2'}
custom_dict["key3"] = "arsh"
custom_dict["key4"] = "mom"

print(custom_dict)

copy_dict = custom_dict.copy()

# Clear the original dictionary
custom_dict.clear()

print(custom_dict)  # Output: {}
print(copy_dict)

value = custom_dict.setdefault('key2', 'new_value')
print(value)
print(custom_dict)
#
# value = custom_dict.pop("key1")
# print(value)
# print(custom_dict)



# del d[2]
# print(d)
# all_keys = d.keys()
# print(all_keys)