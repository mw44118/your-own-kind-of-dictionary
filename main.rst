+++++++++++++++++++++++++++
Your own kind of dictionary
+++++++++++++++++++++++++++

.. contents::

Introduction
============

This article walks through my experience when I tried to do something
that seemed really simple -- make an object that acts just like a
regular dictionary, but with a specialized __str__ method so that it
prints out differently, and with some restrictions on the values for
certain keys.

It took me way longer than I expected to find a solution that did
everything.

What I want
===========

I'm working on a project-management system.  I want to store a task as
an object that is essentially a dictionary, except with a few extra
features, constraints, and methods added on.

What do I need my object to do
==============================

1.  I want to tweak __str__ so that instances look like this when printed::

        >>> from task import Task
        >>> t = Task(
        ...     title='Wash dishes',
        ...     importance='not very important',
        ...     difficulty='easy')

        >>> print(t)
        Wash dishes
        ===========

        Attributes
        ----------

        difficulty            : easy
        importance            : not very important


2.  I want to restrict allowed values for a few keys to just the
    elements in a set, like this::

        >>> Task.allowed_values
        {}

        >>> Task.allowed_values['difficulty'] = set([
        ...     'easy', 'straightforward', 'difficult',
        ...     'maybe impossible'])


    Then when I insert anything but an allowed value, I want a
    ValueError like this::

        >>> t['difficulty'] = 'no problem'
        ...
        Traceback!

        ValueError...

3.  I want to restrict allowed types for a few keys in a similar way,
    like this::

        >>> Task.allowed_types
        {}

        >>> Task.allowed_types['finished'] = bool

    And it should raise a TypeError when the attribute isn't an instance
    of that type::

        >>> t['finished'] = 'your mom'
        ...
        Traceback!

        TypeError...


4.  Finally, I want to take advantage of `pep 3119`_ and make it easy for
    other people to test if my object is an instance of
    collections.Mapping::

        >>> import collections
        >>> isinstance(t, collections.Mapping)
        True

.. _`pep 3119`: http://www.python.org/dev/peps/pep-3119/


I'll get into what I like about PEP3119 later, but the main idea is that
external code needs some way to tell if my object can "quack like" a
dictionary.  In other words, I want to advertise that my class supports
methods like looking up a value by a key, iterating through the keys,
etc.

Something vaguely like TDD
==========================

I think that in order to strictly comply with what people call TDD, I
would write just a single test and then write just enough code to
satisfy this test.

Instead, I'm going to write several tests at a time, then write some
code to satisfy all those tests.  Then I'll write some more tests.

Or maybe after I get my code to pass all the tests once, I'll go back
and reorganize it to make it not so ugly.


