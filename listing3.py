# vim: set expandtab ts=4 sw=4 filetype=python:

import unittest

class TestAsString(unittest.TestCase):

    def test_1(self):
        """
        Convert an empty TaskDict to a string.
        """

        td = Task()
        s = str(td)

        assert s == 'Empty task', \
        """Expected 'Empty task', got %s!""" % s


    def test_2(self):
        """
        Convert a Task with stuff inside it into a string.
        """

        td = Task(title='Waterproof basement',
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


class TestAllowedValues(unittest.TestCase):

    def setUp(self):

        td = Task()

        td.allowed_values = dict(

            difficulty=set(['easy', 'straightforward', 'difficult',
                'maybe impossible']),

        )

        self.td = td


    def test_1(self):
        """
        Verify regular insertions work fine.
        """

        assert 'difficulty' not in self.td
        self.td['difficulty'] = 'easy'
        assert self.td['difficulty'] == 'easy'


    def test_2(self):
        """
        Verify we can restrict a key to a set of values.
        """

        self.assertRaises(KeyError,
            lambda: self.td.__setitem__('easy', 'trivial'))



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





if __name__ == '__main__':
    unittest.main()
