# vim: set expandtab ts=4 sw=4 filetype=python:

import unittest

import listing2

"""
Write a task that uses composition, not inheritance.
"""

class TestAsString(listing2.TestAsString):

    def setUp(self):
        self.Task = Task

class TestRestrictToSets(listing2.TestRestrictToSets):

    def setUp(self):
        self.Task = Task

class TestRestrictToTypes(listing2.TestRestrictToTypes):

    def setUp(self):
        self.Task = Task


class TestDictUtilityMethods(unittest.TestCase):

    """
    Test a bunch of methods that people expect to use on dictionaries.
    """

    def setUp(self):
        self.Task = Task

    def test_keys(self):

        t = self.Task(title='wash dishes', importance='not very')
        assert sorted(t.keys()) == ['importance', 'title']

    def test_values(self):

        t = self.Task(title='wash dishes', importance='not very')
        assert sorted(t.values()) == ['not very', 'wash dishes']

    def test_items(self):

        t = self.Task(title='wash dishes', importance='not very')

        assert sorted(t.items()) == [
            ('importance', 'not very'), ('title', 'wash dishes')], \
        'Got %s! expected something else.' % sorted(t.items())

    def test_pop(self):
        t = self.Task(title='wash dishes', importance='not very')
        t.pop('importance')
        assert 'importance' not in t.keys()

    def test_contains(self):
        t = self.Task(title='wash dishes', importance='not very')
        assert 'title' in t

    def test_copy(self):
        t = self.Task(title='wash dishes', importance='not very')
        copy_of_t = t.copy()

        for k, v in t.items():
            assert t[k] is copy_of_t[k]

    def test_iterate_through_keys(self):
        t = self.Task(title='wash dishes', importance='not very')
        assert sorted(list(t)) == ['importance', 'title']

class Task(object):

    def __init__(self, d=None, **kwargs):

        self._d = dict()

        if isinstance(d, dict):

            for k, v in d.items():
                self.__setitem__(k, v)

        if kwargs:
            for k, v in kwargs.items():
                self.__setitem__(k, v)

    def __getitem__(self, k):
        return self._d[k]

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

        self._d[k] = v


    def update(self, d, **kwargs):

        if hasattr(d, 'keys'):

            for k in d.keys():
                self.__setitem__(k, d[k])

        for k, v in kwargs.items():
                self.__setitem__(k, d[k])


    def __str__(self):

        if not self._d:
            return "Empty task"

        else:

            return "\n".join(
                [
                    self._d['title'],
                    "="*len(self._d['title']),
                    "",
                    "Attributes",
                    "-"*len("Attributes"),
                    ""]
                + [
                    "%-31s: %s" % (k, v)
                    for k, v in self._d.items()
                    if k != 'title']
                + [""]
                )


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


if __name__ == '__main__':
    unittest.main()
