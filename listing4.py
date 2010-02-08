# vim: set expandtab ts=4 sw=4 filetype=python:

import unittest, UserDict

import listing3


class TestAsString(listing3.TestAsString):

    def setUp(self):
        self.Task = Task

class TestRestrictToSets(listing3.TestRestrictToSets):

    def setUp(self):
        self.Task = Task

class TestRestrictToTypes(listing3.TestRestrictToTypes):

    def setUp(self):
        self.Task = Task

class TestDictUtilityMethods(listing3.TestDictUtilityMethods):

    def setUp(self):
        self.Task = Task


class Task(UserDict.UserDict):

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


    def __str__(self):

        if not self.data:
            return "Empty task"

        else:

            return "\n".join(
                [
                    self.data['title'],
                    "="*len(self.data['title']),
                    "",
                    "Attributes",
                    "-"*len("Attributes"),
                    ""]
                + [
                    "%-31s: %s" % (k, v)
                    for k, v in self.data.items()
                    if k != 'title']
                + [""]
                )


class InheritedTask(Task):

    """
    Show how super doesn't work on UserDict.UserDict.
    """

    def __str__(self):
        return super(InheritedTask, self).__str__()

class TestInheritedTaskAsString(TestAsString):

    def setUp(self):
        self.Task = InheritedTask


if __name__ == '__main__':
    unittest.main()
