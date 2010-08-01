# vim: set expandtab ts=4 sw=4 filetype=python:

import unittest

from junkyard import Movie, FailDict

class TestFavorites(unittest.TestCase):

    def setUp(self):

        allowed_colors = set(['red', 'green', 'blue'])

        class Favorites(FailDict):

            allowed_sets = {
                'color':allowed_colors,
                'season':set(['summer', 'spring', 'winter', 'fall'])
            }

            allowed_types = {
                'movie': Movie,
                'integer': int
            }

        self.Favorites = Favorites

    def test_1(self):
        "This one should work just fine."

        f = self.Favorites()
        f['color'] = 'red'
        f['movie'] = Movie('Pootie Tang')

    def test_2(self):
        """
        Verify we can't store a non-color with the color key.
        """

        f = self.Favorites()
        self.assertRaises(
            ValueError,
            f.__setitem__,
            *('color', 'squant'))

    def test_3(self):

        """
        Verify we can't store anything but an instance of the Movie
        class for a movie.
        """

        f = self.Favorites()
        self.assertRaises(
            TypeError, f.__setitem__, *('movie', 99))


if __name__ == '__main__':
    unittest.main()
