# vim: set expandtab ts=4 sw=4 filetype=python:

import unittest

import test3

from junkyard import Movie, CompositeDict

class TestCompositeFavorites(test3.TestFavoritesEvenMore):

    """
    Rerun the tests on the composite implementation.
    """

    def setUp(self):

        allowed_colors = set(['red', 'green', 'blue'])

        class Favorites(CompositeDict):

            allowed_sets = {
                'color':allowed_colors,
                'season':set(['summer', 'spring', 'winter', 'fall'])
            }

            allowed_types = {
                'movie': Movie,
                'integer': int
            }

        self.Favorites = Favorites

if __name__ == '__main__':
    unittest.main()
