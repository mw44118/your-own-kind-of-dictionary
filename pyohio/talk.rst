++++++++++++++++++++++++++++++++++++
Building your own kind of dictionary
++++++++++++++++++++++++++++++++++++

.. contents::

What I want
===========

I want an object like a regular dictionary, except I want to restrict
values for some keys.

For example, pretend I have a class called Favorites, and I want this
code to work fine::

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

*   The FailDict is a placeholder.

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
>>>>>>> fbe765ed35b68c6029dd41dc0da38c992bcfe2a2:pyohio/talk.rst


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

This approach gets around the issues in the first implementation::

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

The standard library has a UserDict module with a UserDict class inside.
Back in olden times, it wasn't possible to subclass dict directly.

This one sucks.  First of all, it fails at test_4 and test_5, which are
the tests that make sure that __init__ and update use our special
homemade __setitem__ method::

    $ python test5.py
    ...FF
    ======================================================================
    FAIL: test_4 (__main__.TestUserDict)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File
    "/home/matt/checkouts/your-own-kind-of-dictionary/pyohio/test3.py",
    line 23, in test_4
    **{'color': 'squant'})
    AssertionError: ValueError not raised

    ======================================================================
    FAIL: test_5 (__main__.TestUserDict)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File
    "/home/matt/checkouts/your-own-kind-of-dictionary/pyohio/test3.py",
    line 37, in test_5
    d)
    AssertionError: TypeError not raised

    ----------------------------------------------------------------------
    Ran 5 tests in 0.001s

    FAILED (failures=2)


But that is fixable -- I would need to write my own __init__ and update
to force it.  Which is yucky, but not a complete show-stopper.


More UserDict.UserDict failure
==============================

The code in the setUp method test6.py subclasses Favorites to add a
little debugging stuff.

Then it runs one single easy test -- test_1 -- that does some simple
sets and then gets.  And KABOOM::

    (master)$ python test6.py
    Inside __setitem__ with key color and value red
    E
    ======================================================================
    ERROR: test_1 (__main__.TestUserDictSuper)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "test6.py", line 46, in test_1
    f['color'] = 'red'
    File "test6.py", line 36, in __setitem__
    super(NoisyFavorites, self).__setitem__(k, v)
    TypeError: super() argument 1 must be type, not classobj

    ----------------------------------------------------------------------
    Ran 1 test in 0.001s

    FAILED (errors=1)

Notice this line::

    TypeError: super() argument 1 must be type, not classobj

UserDict.UserDict is an old-style class, meaning it is defined like
this::

    class UserDict:

and not like this instead::

    class UserDict(object):

This has some non-obvious and annoying consequences on UserDict.  The
super function does different things on old-style classes and new-style
classes.

It makes sense that UserDict.UserDict is not a new-style class, since it
was written before new-style classes were invented, and one of the
points of new-style classes was to allow people to subclass the built-in
types.

On to UserDict.DictMixin
========================

The test7.py file imports my DictMixinSubclass and then subclasses it
and then runs all the old tests again::

    (master)$ python test7.py
    Inside __setitem__ with key color and value red
    Inside __setitem__ with key movie and value Pootie Tang
    .Inside __setitem__ with key color and value squant
    .Inside __setitem__ with key movie and value 99
    .Inside __setitem__ with key color and value squant
    .Inside __setitem__ with key integer and value 99.99
    .
    ----------------------------------------------------------------------
    Ran 5 tests in 0.001s

    OK

Notice those noisy print statements -- those show we're able to use the
super keyword.  And all the old tests pass.  Hurray!!!

DictMixinSubclass implementation
================================

I'm using the same approach as the composition-based dictionary from
earlier, but I don't have to implement all those related methods.
Instead, as long as I define these methods:

*   __init__
*   __delitem__
*   __getitem__
*   __setitem__
*   keys

Then the DictMixin will do the right thing for all the other methods,
like update, items, values, setdefault, __contains__, __iter__, pop,
popitem, and many, many more.

But wait -- there's more
========================

If you're using python2.6 or later, there's something even better than
UserDict.DictMixin.  PEP 3109 introduced the idea of an abstract base
class (ABC) to python.

ABCs enforce requirements
=========================

Through metaclass tomfoolery, python makes sure you are defining
everything you need to define in order to fulfill the interface.
For example, an ABC will help you if you forget to define everything
you have to.

When I say "help you", I mean it will blow up when the class is
defined::

    >>> class MutableMappingSubclass(collections.MutableMapping):
    ...     pass
    >>>
    >>> MutableMappingSubclass()
    ------------------------------------------------------------
    Traceback (most recent call last):
      File "<ipython console>", line 1, in <module>
      TypeError: Can't instantiate abstract class MutableMappingSubclass
      with abstract methods __delitem__, __getitem__, __iter__, __len__,
      __setitem__

You don't get that kind of protection with
DictMixin::

    >>> class DictMixinSubclass(object, UserDict.DictMixin):
    ...     pass
    ...
    >>> DictMixinSubclass()
    <__main__.DictMixinSubclass object at 0xa0bb7ec>


ABCs announce "I can quack like a dictionary"
=============================================

With all these different ways to emulate dictionary behavior, it was
never easy to take an unknown object and then ask it if it supports a
dictionary-like interface.

1.  You can use hasattr to check for the existence of methods like
    __getitem__ and keys, but you'll get a false negative on objects
    using __getattr__ hooks.

2.  You can use isinstance(dict), but that will fail for stuff like my
    composition-based approach and the UserDict.DictMixin approach.

But if you subclass from collections.MutableMapping, then you are OK.

THE END
