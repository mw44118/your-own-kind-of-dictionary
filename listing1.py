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


# Uncomment the next lines to see the difference between errors and
# failures.
# class Task(object):
#     def __init__(self, *args, **kwargs):
#         pass


if __name__ == '__main__':
    unittest.main()
