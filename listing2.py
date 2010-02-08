# vim: set expandtab ts=4 sw=4 filetype=python:

import unittest

import listing1

class TestAsString(listing1.TestTaskAsString):

    def setUp(self):
        self.Task = Task


class TestRestrictToSets(unittest.TestCase):

    def setUp(self):
        self.Task = RestrictedValueTask

    def test_good_value(self):
        """
        Verify we can set a key to an allowed value.
        """

        t = self.Task()

        t.allowed_sets = {
            'favorite color': set(['red', 'blue' 'yellow', 'green'])}

        t['favorite color'] = 'red'
        assert t['favorite color'] == 'red'


    def test_bad_value(self):
        """
        Verify that assigning to a value not in the set raises a
        ValueError.
        """

        t = self.Task()

        t.allowed_sets = {
            'favorite color': set(['red', 'blue', 'yellow', 'green'])}

        def set_an_invalid_color():
            t['favorite color'] = 'pink'

        self.assertRaises(ValueError, set_an_invalid_color)


class TestRestrictToTypes(unittest.TestCase):

    def setUp(self):
        self.Task = RestrictedValueTask

    def test_allowed_type(self):
        """
        Verify we can set a key to an allowed type.
        """

        t = self.Task()

        t.allowed_types = {
            'temperature':int,
        }

        t['temperature'] = 99
        assert t['temperature'] == 99

    def test_bad_value(self):
        """
        Verify that assigning to a value not in the set raises a
        ValueError.
        """

        t = self.Task()

        t.allowed_types = {
            'temperature':int,
        }

        def set_an_invalid_temperature():
            t['temperature'] = 'pink'

        self.assertRaises(ValueError, set_an_invalid_temperature)


    def test_init(self):

        """
        Verify __init__ uses our __setitem__ method.
        """

        self.Task.allowed_types = {
            'temperature':int,
        }

        def set_an_invalid_temperature():
            t = self.Task(temperature='pink')

        self.assertRaises(ValueError, set_an_invalid_temperature)


    def test_update(self):

        """
        Verify update uses our __setitem__ method.
        """

        self.Task.allowed_types = {
            'temperature':int,
        }

        def set_an_invalid_temperature():
            t = self.Task()
            t.update({'temperature':'pink'})

        self.assertRaises(ValueError, set_an_invalid_temperature)


class RestrictedValueTask(listing1.RefactoredTask):

    """
    Has the code to restrict values to members of sets or instances of
    types.
    """

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

        super(Task, self).__setitem__(k, v)


if __name__ == '__main__':
    unittest.main()
