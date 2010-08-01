# vim: set expandtab ts=4 sw=4 filetype=python:

import unittest

import test2

class TestFavoritesEvenMore(test2.TestFavoritesAgain):

    """
    Add a few more tests for our subclassed dictionary.
    """

    def test_4(self):
        """
        Make sure this code blows up with a ValueError:

        self.Favorites({'color': 'squant'})
        """

        self.assertRaises(
            ValueError,
            self.Favorites,
            **{'color': 'squant'})


    def test_5(self):
        """
        Test the update function.
        """

        d = {'integer': 99.99}
        f = self.Favorites()

        self.assertRaises(
            TypeError,
            f.update,
            d)


if __name__ == '__main__':
    unittest.main()

