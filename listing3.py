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


class Task(object):

    def __init__(self, d=None, **kwargs):

        self._d = dict()

        if isinstance(d, dict):
            self._d.update(d)

        if kwargs:
            self._d.update(kwargs)

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
        self._d.update(d, **kwargs)


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

if __name__ == '__main__':
    unittest.main()
