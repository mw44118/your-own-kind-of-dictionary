# vim: set expandtab ts=4 sw=4 filetype=python:


import collections, unittest, UserDict
import task


class TestTask(unittest.TestCase):

    def tearDown(self):
        del(self.t)

    def test_str(self):
        """
        Verify we can alter __str__
        """

        assert str(self.t) == 'I have a tweaked __str__ method!'

    def test_setitem_1(self):
        """
        Verify we can restrict allowed vaues
        """

        self.assertRaises(ValueError, self.t.__setitem__, 'color', 'happy')

    def test_setitem_2(self):
        """
        Verify update() uses my __setitem__.
        """
        self.assertRaises(ValueError, self.t.update, {'color':'happy'})

    def test_iterate(self):
        """
        Verify we can iterate through keys
        """

        assert sorted(list(self.t)) == ['a', 'b']


    def test_contains(self):
        """
        Verify we can test if a key is in the object
        """

        assert 'a' in self.t
        assert 'b' in self.t

    def test_isinstance(self):
        """
        Verify t is an instance of collections.Mapping
        """

        assert isinstance(self.t, collections.Mapping)


class TestFancyDict(TestTask):

    def setUp(self):
        self.t = task.FancyDict({'a':1, 'b':2})


if __name__ == '__main__':
    unittest.main()

