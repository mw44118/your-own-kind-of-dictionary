# vim: set expandtab ts=4 sw=4 filetype=python:

"""
I want a regular dictionary, but with some changes:

1.  I want to tweak __str__.
2.  I want to restrict allowed values for some keys.
3.  I want to restrict allowed types for some keys.
4.  I want the object to be an instance of collections.MutableMapping.

This file tracks my effort to get those two simple tasks done.
"""

import collections, UserDict


    class BoringDict(dict):

        # Restrict values for certain keys.
        allowed_values = {}

        def __str__(self):
            return "I have a tweaked __str__ method!"

        def __setitem__(self, k, val):

            if k in self.allowed_values \
            and val not in self.allowed_values[k]:

                raise ValueError(
                    "Sorry, values for key %s must be one of %s!"
                    % (k, self.allowed_values[k]))

            else:
                self.data[k] = val


    class FancyDict(BoringDict):

        allowed_values = {
            'color':['red', 'green', 'blue'],
            'feeling':['happy', 'sad'],
        }

        def __str__(self):

            s = super(FancyDict, self).__str__()
            return s.replace('boring', 'fancy')


    class BoringUserDict(UserDict.UserDict):

        # Restrict values for certain keys.
        allowed_values = {}

        def __str__(self):
            return "I am a boring UserDict subclass!"

    def __setitem__(self, k, val):

        if k in self.allowed_values \
        and val not in self.allowed_values[k]:

            raise ValueError(
                "Sorry, values for key %s must be one of %s!"
                % (k, self.allowed_values[k]))

        else:
            self.data[k] = val


class FancyUserDict(BoringUserDict):

    allowed_values = {
        'color':['red', 'green', 'blue'],
        'feeling':['happy', 'sad'],
    }

    def __str__(self):

        s = super(FancyUserDict, self).__str__()
        return s.replace('boring', 'fancy')


class BoringDictMixin(object, UserDict.DictMixin):

    # Restrict values for certain keys.
    allowed_values = {}

    def __init__(self, d=None, **kwargs):
        if d and not kwargs:
            self.data = d
        elif kwargs:
            self.data = kwargs
        else:
            self.data = {}

    def __str__(self):
        return "I am a boring DictMixin subclass!"

    def __getitem__(self, k):
        return self.data[k]

    def __setitem__(self, k, val):

        if k in self.allowed_values \
        and val not in self.allowed_values[k]:

            raise ValueError(
                "Sorry, values for key %s must be one of %s!"
                % (k, self.allowed_values[k]))

        else:
            self.data[k] = val

    def keys(self):
        return self.data.keys()


class FancyDictMixin(BoringDictMixin):

    allowed_values = {
        'color':['red', 'green', 'blue'],
        'feeling':['happy', 'sad'],
    }

    def __str__(self):

        s = super(FancyDictMixin, self).__str__()
        return s.replace('boring', 'fancy')


class BoringMutableMappingSubclass(collections.MutableMapping):

    # Restrict values for certain keys.
    allowed_values = {}

    def __init__(self, d=None, **kwargs):
        if d and not kwargs:
            self.data = d
        elif kwargs:
            self.data = kwargs
        else:
            self.data = {}

    def __str__(self):
        return "I am a boring MutableMapping subclass!"

    def __getitem__(self, k):
        return self.data[k]

    def __setitem__(self, k, val):

        if k in self.allowed_values \
        and val not in self.allowed_values[k]:

            raise ValueError(
                "Sorry, values for key %s must be one of %s!"
                % (k, self.allowed_values[k]))

        else:
            self.data[k] = val


    def __delitem__(self, k):
        self.data.__delitem__(k)


    def __iter__(self):
        return iter(self.data)


    def __len__(self):
        return len(self.data)


    def keys(self):
        return self.data.keys()


class FancyMutableMappingSubclass(BoringMutableMappingSubclass):

    allowed_values = {
        'color':['red', 'green', 'blue'],
        'feeling':['happy', 'sad'],
    }

    def __str__(self):

        s = super(FancyMutableMappingSubclass, self).__str__()
        return s.replace('boring', 'fancy')


