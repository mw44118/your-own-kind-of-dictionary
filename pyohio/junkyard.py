# vim: set expandtab ts=4 sw=4 filetype=python:

import UserDict

class Movie(str):
    """
    Movies are fun.
    """

class FailDict(object):

    def __setitem__(self, k, v):
        pass

class SubclassDict(dict):
    """
    First real effort.
    """

    def __setitem__(self, k, v):

        allowed_sets = getattr(self, 'allowed_sets', {})
        allowed_types = getattr(self, 'allowed_types', {})

        if k in allowed_sets:

            s = allowed_sets[k]

            if v not in s:

                raise ValueError(
                    "Sorry, but values for %s must be in %s!"
                    % (k, s))

        if k in allowed_types:

            cls = allowed_types[k]

            if not isinstance(v, cls):

                raise TypeError(
                    "Sorry, but values for %s must be instances of %s!"
                    % (k, cls))

        super(SubclassDict, self).__setitem__(k, v)


class CompositeDict(object):

    def __init__(self, d=None, **kwargs):

        self._d = dict()

        if isinstance(d, dict):

            for k, v in d.items():
                self.__setitem__(k, v)

        if kwargs:
            for k, v in kwargs.items():
                self.__setitem__(k, v)

    def __setitem__(self, k, v):
        allowed_sets = getattr(self, 'allowed_sets', {})
        allowed_types = getattr(self, 'allowed_types', {})

        if k in allowed_sets \
        and v not in allowed_sets[k]:

            raise ValueError(
                "%s must be one of %s, not %s!"
                % (k, allowed_sets[k], v))

        if k in allowed_types \
        and not isinstance(v, allowed_types[k]):

            raise TypeError(
                "%s must be an instance of %s, not %s!"
                % (k, allowed_types[k], type(v)))

        self._d[k] = v

    def update(self, d, **kwargs):

        if hasattr(d, 'keys'):

            for k in d.keys():
                self.__setitem__(k, d[k])

        for k, v in kwargs.items():
                self.__setitem__(k, d[k])

    def keys(self):
        return self._d.keys()

    def values(self):
        return self._d.values()

    def __getattr__(self, attrname):
        return getattr(self._d, attrname)

    def __contains__(self, element):
        return element in self._d

    def __iter__(self):
        return iter(self._d)


class UserDictSubclass(UserDict.UserDict):

    def __setitem__(self, k, v):

        allowed_sets = getattr(self, 'allowed_sets', {})
        allowed_types = getattr(self, 'allowed_types', {})

        if k in allowed_sets \
        and v not in allowed_sets[k]:

            raise ValueError(
                "%s must be one of %s, not %s!"
                % (k, allowed_sets[k], v))

        if k in allowed_types \
        and not isinstance(v, allowed_types[k]):

            raise ValueError(
                "%s must be an instance of %s, not %s!"
                % (k, allowed_types[k], type(v)))

        self.data.__setitem__(k, v)


