# vim: set expandtab ts=4 sw=4 filetype=python:

import unittest

class TestAsString1(unittest.TestCase):
    """
    This one is going to raise ERRORs.
    """

    def test_1(self):
        """
        Convert an empty TaskDict to a string.
        """

        td = self.Task()
        s = str(td)

        assert s == 'Empty task', \
        """Expected 'Empty task', got %s!""" % s


    def test_2(self):

        """
        Convert a Task with stuff inside it into a string.
        """

        td = self.Task(title='Waterproof basement',
            expected_cost_range=[3000, 8000])

        s = str(td)

        expected_results = """\
Waterproof basement
===================

Attributes
----------

expected_cost_range            : [3000, 8000]
"""

        assert s == expected_results, \
        "Got %s, expected something different!" % s


class Task(dict):
    """
    Just like a dictionary, but with modified __str__ and __setitem__
    methods.
    """

    def __str__(self):
        if not self:
            return "Empty task"

        else:

            return "\n".join(
                [
                    self['title'],
                    "="*len(self['title']),
                    "",
                    "Attributes",
                    "-"*len("Attributes"),
                    ""]
                + [
                    "%-31s: %s" % (k, v)
                    for k, v in self.items()
                    if k != 'title']
                + [""]
                )


class NullTask(object):
    def __init__(self, *args, **kwargs):
        pass


class TestAsString2(TestAsString1):

    def setUp(self):
        self.Task = NullTask


class TestAsString3(TestAsString1):

    """
    This one should pass.
    """

    def setUp(self):
        self.Task = Task



if __name__ == '__main__':
    unittest.main()
