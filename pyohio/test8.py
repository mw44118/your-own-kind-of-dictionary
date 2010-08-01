# vim: set expandtab ts=4 sw=4 filetype=python:

import collections
import unittest

import test3

from junkyard import Movie, MutableMappingSubclass

class TestIncompleteSpecification(unittest.TestCase):

    """
    Rerun the tests on the UserDict.UserDict sublcass.
    """

    def setUp(self):

        allowed_colors = set(['red', 'green', 'blue'])

        class Favorites(MutableMappingSubclass):

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

    def test_6(self):





if __name__ == '__main__':
    unittest.main()
