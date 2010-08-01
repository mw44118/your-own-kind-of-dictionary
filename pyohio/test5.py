# vim: set expandtab ts=4 sw=4 filetype=python:

import unittest

import test4

from junkyard import Movie, UserDictSubclass

class TestUserDict(test4.TestCompositeDict):

    """
    Rerun the tests on the UserDict.UserDict sublcass.
    """

    def setUp(self):

        allowed_colors = set(['red', 'green', 'blue'])

        class Favorites(UserDictSubclass):

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
