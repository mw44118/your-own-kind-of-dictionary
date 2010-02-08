# vim: set expandtab ts=4 sw=4 filetype=python:

import collections, unittest, UserDict

import listing4

class Task(object, UserDict.DictMixin):

    def __init__(self, d=None, **kwargs):
        self._d = {}

        if isinstance(d, dict):
            for k in d:
                self[k] = d[k]

        for k in kwargs:
            self[k] = kwargs[k]

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

        self._d.__setitem__(k, v)

    def keys(self):
        return self._d.keys()

    def __delitem__(self, k):
        self._d.__delitem__(k)

    # def copy(self):
        # return Task(self._d.copy())

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

class TestAsString(listing4.TestAsString):

    def setUp(self):
        self.Task = Task

class TestRestrictToSets(listing4.TestRestrictToSets):

    def setUp(self):
        self.Task = Task

class TestRestrictToTypes(listing4.TestRestrictToTypes):

    def setUp(self):
        self.Task = Task

class TestDictUtilityMethods(listing4.TestDictUtilityMethods):

    def setUp(self):
        self.Task = Task

class InheritedTask(Task):

    def __str__(self):
        return super(InheritedTask, self).__str__()


class TestInheritedTaskAsString(TestAsString):

    def setUp(self):
        self.Task = InheritedTask


class TestPEP3119(unittest.TestCase):

    def setUp(self):
        self.Task = Task

    def test_1(self):

        t = self.Task()

        assert isinstance(t, collections.MutableMapping), \
        't is an instance of %s!' % type(t)

if __name__ == '__main__':
    unittest.main()
