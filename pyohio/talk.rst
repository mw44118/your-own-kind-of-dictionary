++++++++++++++++++++++++++++++++++++
Building your own kind of dictionary
++++++++++++++++++++++++++++++++++++

.. contents::

What kind of object I want
==========================

It should act like a regular dictionary, except it allows instances to
restrict values for keys in different ways

1.  Restrict values for a particular key to a set.  For example, I
    want to have a key 'best Doctor Who companion' that requires a
    choice between 'Leela' and 'Rose'.

2.  Require all values to be instances a certain class.  This is
    similar to what you get in SQL when you declare a column to be
    a certain type, except I want to allow subclasses of types to be
    OK.

    For example, imagine that the "birthday" key requires the
    value to be an instance of a datetime.date class.

3.  Allow storing a callable for each key and store the results of
    running the key and value through that callable.

    For example, maybe we want to make sure that the value is a
    prime number.  We can't provide a set of all prime numbers, and
    we can't specify a prime number class.  But we can write a
    function "is_a_prime_number" and make the dictionary do that.


First implementation (subclass dict)
====================================

First I'll subclass dict and then redefine the __setitem__(self, k, v).
I'll check the k and v objects and if everything checks out, I'll store
this key-value pair.  It works like this::

    >>> from junkyard import subclassed_dict
    >>> d = subclassed_dict()
    >>> d.allowed_values = {
    ...     'best Doctor Who companion':set(['Leela', 'Rose'])
    >>> d['best Doctor Who companion'] = 'Leela' # should be OK

    >>> d['best Doctor Who companion'] = 'Ramona' # hell no
    ...

This is the __setitem__ method from my subclassed dictionary.  It only
implements #1 (limit values to elements of a set)::

    def __setitem__(self, k, v):
        """
        This assumes that self.allowed_values exists and is a dictionary
        that maps keys to allowed values for that key.

        """

        if k in allowed_sets \
        and v not in allowed_sets[k]:

            raise ValueError(
                "%s must be one of %s, not %s!"
                % (k, allowed_sets[k], v))

        if k in allowed_types \
        and not isinstance(v, allowed_types[k]):

            raise ValueError(
                "%s must be an instance of %s, not %s!"
                % (k, allowed_types[k], type(v)))

        super(Task, self).__setitem__(k, v)





How the implementation is defined
---------------------------------

Examine test results
--------------------

The tests show that the subclassed __setitem__ method won't get called
from the parent class.

Examine C code behind dict
--------------------------

It wasn't obvious to me why I got this error.  I asked around and was
told to read XXXXX.c to understand...

Composition-based implementation
================================

Composition vs inheritance
--------------------------

Examine test results
--------------------

Add methods to the container
----------------------------

Point out irritating need to manually redefine every related dictionary
method on the container class

Use __getattr__
----------------

Show how to use __getattr__ to avoid all that boring wrapper code

__getattr__ ruins inspection
----------------------------

__getattr__ doesn't play nice with inspection tools

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
