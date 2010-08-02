# vim: set expandtab ts=4 sw=4 filetype=python:

import unittest

import test3

from junkyard import Movie, DictMixinSubclass

class TestSubclassedFavorites(test3.TestFavoritesEvenMore):

    """
    Rerun the tests on the UserDict.UserDict sublcass.
    """

    def setUp(self):

        allowed_colors = set(['red', 'green', 'blue'])

        class Favorites(DictMixinSubclass):

            allowed_sets = {
                'color':allowed_colors,
                'season':set(['summer', 'spring', 'winter', 'fall'])
            }

            allowed_types = {
                'movie': Movie,
                'integer': int
            }

        class NoisyFavorites(Favorites):

            def __setitem__(self, k, v):
                print "Inside __setitem__ with key %s and value %s" % (k, v)

                super(NoisyFavorites, self).__setitem__(k, v)

        self.Favorites = NoisyFavorites


if __name__ == '__main__':
    unittest.main()
