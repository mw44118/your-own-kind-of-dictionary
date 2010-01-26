+++++++++++++++++++++++++++
Your own kind of dictionary
+++++++++++++++++++++++++++

.. contents::

What I want
===========

I'm working on a project-management system.  I want to store a task as
an object that is essentially a dictionary, except with a few extra
features, constraints, and methods added on.

Getting everything just right took me way more time than I expected.
This article describes the dead ends I ran into along the way to the
solution that I'm happy with.

Why I want a dictionary
=======================

Don't get me wrong -- I love relational databases.  But I'm tired of
them.  And I wanted to explore what happens when a system has a
schema-free database at the core.

Here's how I use this system to keep track of the myriad home
improvement tasks I've got in mind::

    >>> from xxx import HomeImprovementTask as Task
    >>> t1 = Task(title='waterproof basement',
    ...     expected_cost_range=[3000, 8000])

    >>> t2 = Task(title='paint or stain deck',
    ...     expected_cost_range=[200, 1000])

    >>> t3 = Task(title='Renovate kitchen',
    ...     expected_cost_range=[8*1000, 20*1000])

For home improvment stuff, I use an attribute named **expected cost
range** to point to a two-element list of numbers, that just happen to
mean the lower and upper bounds of what I expect to spend on the
project.

Meanwhile, here's how I might keep track of the tasks involved in
writing this article::

    >>> from xxx import WritingTask as Task
    >>> from datetime import date
    >>> t1 = Task(title='Write outline', due_date=date(2009, 12, 31),
    ...     finished=True)

    >>> t2 = Task(title='Write code samples',
    ...     depends_on=t1,
    ...     due_date=date(2010, 1, 4),
    ...     finished=False)

    >>> t3 = Task(title='Write explanations of code',
    ...     due_date=date(2010, 1, 11),
    ...     depends_on=t2,
    ...     finished=False)

    >>> t4 = Task(title='Finish and submit article',
    ...     due_date=date(2010, 1, 18),
    ...     depends_on=t3,
    ...     finished=False)


This one has datetime.date values for an attribute named **due date**
a **depends_on** attribute that points to another task, and a boolean
**finished** attribute.

So the main idea is that different projects use different key-value
pairs and I don't want to guess the entire universe of attributes
and values I'm going to need ahead of time.


What do I need my object to do
==============================

1.  I want to tweak __str__ so that it looks like this when printed::

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


2.  I want to restrict allowed values for a few keys like this::

        >>> Task.allowed_values
        {}

        >>> Task.allowed_values['difficulty'] = [
        ...     'easy', 'straightforward', 'difficult',
        ...     'maybe impossible']


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


I'll get into what I like about PEP3119 way later.


Possible ways to build it
=========================

Here's a short list of ideas I came up with:

1.  Subclass the builtin dict class.

2.  Don't subclass anything (except for object).  Just define for myself
    all the methods like __getitem__, __setitem__, etc.

3.  Subclass the UserDict.UserDict class.

4.  Subclass the UserDict.DictMixin class.


I'll use tests to, err, test the different ways to build it
===========================================================

I'll follow a pattern throughout this article that looks roughly like
this:

1.  I'll write some code to verify the object (sometimes people call
    this the system under test, or SUT) does what I want it to do.  You
    can think of the test code as sort of like a specification.

2.  I'll run the test and verify I get a failure.  It's important to
    keep track of the difference between failures and errors in test
    code.  I want a failure, not an error.  A failure shows a problem in
    the SUT.  An error means somehow the test crashed.  The test might
    have crashed because of an issue in the SUT, or, it might have
    crashed because of a glitch in the

3.  I'll write code on the SUT with the goal in mind of getting the test
    to pass.

4.  I'll rerun the test and see if

Sometimes, in step one, I'll write a single really trivial function.
Other times, I'll write out several variations on the same idea.

Now, at this point, I'll just make it clear to anyone that cares that
I'm not going to be strict about writing just one tiny test and then
just enough code to satisfy this test.  For example, I'll never write a
test that just verifies I can import a module, or just verifies I can
instantiate my subclass.

Instead, I'll write tests for real-life functions, and I'll write
several tests at once.  I've tried other styles, and this one works for
me.


Writing the first test
======================

I want to alter my own dictionary-like object so that when it is
converted to a string, it looks different.  This is easy to write a test
for.  The code in `listing1.py`_ shows how.

.. _`listing1.py`: listing1.py

The last two lines mean that when I run the file as a script, unittest
will run the tests, like this::

    $ python listing1.py
    EE
    ======================================================================
    ERROR: test_1 (__main__.TestAsString)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "listing1.py", line 12, in test_1
        td = Task()
    NameError: global name 'Task' is not defined

    ======================================================================
    ERROR: test_2 (__main__.TestAsString)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "listing1.py", line 25, in test_2
        td = Task(title='Waterproof basement',
    NameError: global name 'Task' is not defined

    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s

    FAILED (errors=2)


Notice the **EE** at the beginning.  Both tests hit an error because they
tried to use a class that wasn't defined.   If you pull the comments off the
code near the bottom of the file, instead of errors, you'll get failures, like
this::

    $ python listing1.py # This time after uncommenting...
    FF
    ======================================================================
    FAIL: test_1 (__main__.TestAsString)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "listing1.py", line 16, in test_1
        """Expected 'Empty task', got %s!""" % s
    AssertionError: Expected 'Empty task', got <__main__.Task object at 0xb76fcf2c>!

    ======================================================================
    FAIL: test_2 (__main__.TestAsString)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "listing1.py", line 41, in test_2
        "Got %s, expected something different!" % s
    AssertionError: Got <__main__.Task object at 0xb76fcf2c>, expected something different!

    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s

    FAILED (failures=2)

Subclass dict
=============



Run test on the dict subclass
=============================

Now add a test to use the update method
=======================================

Run both tests and see what happens
===================================

Discuss how dict subclasses won't use my __setitem__ method in related
methods.

Build a dictionary-like object from scratch
===========================================

Subclass test class to test a different object

Show how to run just a single test class rather than all of them.

Run tests on from-scratch class.

Write a test to use the setdefault method, run it, then extend the
code.

Write a test to iterate through keys, run it, and then extend the code.

Discuss that there should be an easier way rather than building up
EVERYTHING from scratch.

Subclass UserDict.UserDict
==========================

Run existing tests on UserDict.UserDict

Then subclass the subclass of UserDict.UserDict and try to use the super
function.

Discuss what's going on there.  Show the code from the UserDict.UserDict
class.

Subclass UserDict.DictMixin
===========================

Run existing tests on UserDict.DictMixin


What about abstract base classes
================================

Talk about all the ways to guess about an object's nature.

*   try stuff and catch exceptions
*   use hasattr to look for certain methods
*   isinstance tests

Write a test to see if my class is an instance of collections.Mapping
subclass.

Now subclass collections.MutableMapping and rerun our tests.

And we're done!
