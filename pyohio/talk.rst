++++++++++++++++++++++++++++++++++++
Building your own kind of dictionary
++++++++++++++++++++++++++++++++++++

.. contents::

What I want
===========

I want an object like a regular dictionary, except I want to restrict
values for some keys.

For example, pretend I have a class called Favorites, and I want this
code to work just fine::

    f = Favorites()
    f['color'] = 'red'
    f['movie'] = Movie('Pootie Tang')

But I want this code to die a violent death::

    f['color'] = 'squant'

And this one also should die, but for a different reason::

    f['movie'] = 99

The interface
=============

Here's how to define the Favorites class used above::

    allowed_colors = set(['red', 'green', 'blue'])

    class Favorites(RestrictedDict):

        allowed_sets = {
            'color':allowed_colors,
            'season':set(['summer', 'spring', 'winter', 'fall'])
        }

        allowed_types = {
            'movie':Movie,
            'integer':int
        }

Write a few tests
=================

Notice this stuff:

*   The FailDict is just a placeholder.

*   I define my Favorites in the setUp method.

*   I assign self.Favorites to point to that Favorites class.

*   The test_1 method makes an instance of self.Favorites, which is
    really the class defined in setUp, which is a subclass of FailDict.

*   The test_2 method wants to make sure that the code **does** blow up,
    so it uses the unittest.TestCase.assertRaises method and gives it an
    exception, a callable, and some arguments.

    Then the unittest plumbing calls that callable and passes in those
    arguments, and makes sure that the exception we asked for did
    happen.

Results from test1.py
=====================

Here's how to run the tests::

    $ python test1.py
    .FF
    ======================================================================
    FAIL: test_2 (__main__.TestFavorites)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "test1.py", line 43, in test_2
          *('color', 'squant'))
          AssertionError: ValueError not raised

    ======================================================================
    FAIL: test_3 (__main__.TestFavorites)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "test1.py", line 54, in test_3
        TypeError, f.__setitem__, *('movie', 99))
        AssertionError: TypeError not raised

    ----------------------------------------------------------------------
    Ran 3 tests in 0.000s

    FAILED (failures=2)

First implementation (subclass dict)
====================================

This is the __setitem__ method from the SubclassDict class::

    def __setitem__(self, k, v):

        allowed_sets = getattr(self, 'allowed_sets', {})
        allowed_types = getattr(self, 'allowed_types', {})

        if k in allowed_sets:

            s = allowed_sets[k]

            if v not in s:

                raise ValueError(
                    "Sorry, but values for %s must be in %s!"
                    % (k, s))

        if k in allowed_types:

            cls = allowed_types[k]

            if not isinstance(v, cls):

                raise TypeError(
                    "Sorry, but values for %s must be instances of %s!"
                    % (k, cls))

        super(SubclassDict, self).__setitem__(k, v)


Initial test results
====================

The file test2.py applies the tests written in test1.py to a Favorites
class based on SubclassDict, rather than FailDict::

    $ python test2.py
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.000s

    OK


Now add some more tests
=======================

The test3.py file adds two more tests for the subclass dict, and
SubclassDict fails on both::

    $ python test3.py
    ...FF
    ======================================================================
    FAIL: test_4 (__main__.TestFavoritesEvenMore)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "test3.py", line 23, in test_4
        **{'color': 'squant'})
        AssertionError: ValueError not raised

    ======================================================================
    FAIL: test_5 (__main__.TestFavoritesEvenMore)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
        File "test3.py", line 37, in test_5
        d)
        AssertionError: TypeError not raised

    ----------------------------------------------------------------------
    Ran 5 tests in 0.002s

    FAILED (failures=2)


Why SubclassDict fails
======================

The Favorites class is a subclass of SubclassDict which is a subclass of
dict.

The tests show that python doesn't use my own __setitem__ method from
within Favorites.__init__ and Favorites.update.

Why???

This is because the methods __init__ and update on the dict class are
written in C, and they are tightly linked to the C implementation of
__setitem__.

Composition-based implementation
================================

The CompositeDict in junkyard.py take a different approach -- instead of
subclassing dict, it stores a dictionary inside, and then adds methods
on the outside to make it seem like a dictionary subclass.

This approach gets around the nasty issues in the first implementation::

    $ python test4.py
    .....
    ----------------------------------------------------------------------
    Ran 5 tests in 0.001s

    OK

How it works
============

I define __init__ and update to make sure that these methods always use
my __setitem__ method, which does the same stuff as the __setitem__ in
SubclassDict.

Why I don't like it
===================

There are lots of methods besides __getitem__ and __setitem__ on the
dictionary class::

    >>> [k for k in dir({}) if not k.startswith('__')]

    ['clear', 'copy', 'fromkeys', 'get', 'has_key', 'items',
    'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem',
    'setdefault', 'update', 'values']

If I want to offer all these methods with my class, I have to choose one
of these:

1.  Write out all these methods one by one::

        def keys(self):
            return self._d.keys()

    Boring!!!

2.  Use some __getattr__ shenanigans instead::

        def __getattr__(self, attrname):
            return getattr(self._d, attrname)

    But now dir (and other inspection tools) won't be able to see what
    is really going on.

So, I'll put the composition approach in the "maybe" pile.

UserDict.UserDict implementation
================================

Explain implementation
----------------------

Examine test results
--------------------

Add another test
----------------

Add a new test that uses this class as a parent for a subclass

super keyword fail
------------------

Explain how UserDict.UserDict is not a new-style class, so the
super keyword fails.

UserDict.DictMixin
==================

Explain implementation
----------------------

Examine test results
--------------------


PEP 3119
========

duck-typing
-----------

why it is awesome, why it isn't perfect

Add another test
----------------

This test verifies our class is an instance of
collections.MutableMapping.

abstract base classes
---------------------

As of python 2.6, don't use UserDict.DictMixin; use
collections.MutableMapping instead.
