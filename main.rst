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

This article wanders through the following topics:

    *   subclassing built-in types like dict
    *   emulating dictionary behavior without subclassing dict
    *   testing with the standard library unittest module
    *   abstract base classes and PEP 3119

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

Test-driven development (TDD) is a style of development where the
developer writes some test code and then writes just enough code to
satisfy that test.  Then the developer adds a new test, and then writes
enough code to satisfy both tests.  The process looks a little like
this:

    *   write a test
    *   write some code
    *   write a new test
    *   write some new code rewrite the code already there
    *   go back to the top

Often the first tests only focus on a tiny subset of the true required
functionality.  For example, a test might only verify that a module can
be imported, even if the module is empty.

TDD is a great way to write code, but for this article, I'm not going to
be strict about doing TDD exactly by the rules.  Instead, in this
article, I'm going use something vaguely like TDD (SVLTDD).  I'll write
several tests at a time.  My tests will focus on the end result, and
often test compound behaviors that depend on several units all working
correctly.

Then once I have a big enough pile of tests to write something
interesting, I'll write code.  Usually, if I'm just writing code to
satisfy a test, I'll write the worst solution I can think of at first.

Then when I've got something ugly, but functional, I'll go back and
tweak it.  I'll depend on my tests to make sure that my tweaking doesn't
break anything.


Listing one discussion
======================

There's a lot of stuff going on in listing1.py, but I'll walk through it
line by line.  First I wrote a class TestTaskAsString, and the point of
that class is to make sure that my Task class prints out as a string
like how I want.

I hope the two methods easy to understand -- in the first one,
test_as_str_when_empty, I call the __str__ method on my Task instance td
by using the builtin str.
