# vim: set expandtab ts=4 sw=4 filetype=python:

import unittest

from junkyard import Movie, UserDictSubclass

class TestUserDictSuper(unittest.TestCase):

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

        class NoisyFavorites(Favorites):

            def __setitem__(self, k, v):
                print "Inside __setitem__ with key %s and value %s" % (k, v)

                super(NoisyFavorites, self).__setitem__(k, v)

        self.Favorites = NoisyFavorites

    def test_1(self):
        """
        This is a verbatim copy-paste from test1.py
        """

        f = self.Favorites()
        f['color'] = 'red'
        v = f['color']
        self.assertEqual(v, 'red', "Got %s for key color" % v)
        m = Movie('Pootie Tang')
        f['movie'] = m
        self.assertEqual(f['movie'], m)


if __name__ == '__main__':
    unittest.main()
