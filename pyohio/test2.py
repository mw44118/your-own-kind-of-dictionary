# vim: set expandtab ts=4 sw=4 filetype=python:

import unittest

import test1

from junkyard import Movie, SubclassDict

class TestFavoritesAgain(test1.TestFavorites):

    """
    Just like test1.TestFavorites, but self.Favorites is a different
    class.
    """

    def setUp(self):

        allowed_colors = set(['red', 'green', 'blue'])

        class Favorites(SubclassDict):

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
