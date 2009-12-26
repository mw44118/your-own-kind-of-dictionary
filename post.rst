I'm working on a task-management project.  I want to store tasks in
object thats that are essentially dictionaries, except with a few extra
features, constraints, and methods added on.

Getting everything just right took me way more time than I expected.


What do I need my object to do
==============================

Pretend my class that is named Task.  And it can be used just like a
regular dictionary; e.g.::

    >>> from task import Task
    >>> t = Task(
    ...     title='Wash dishes',
    ...     importance='not very important',
    ...     difficulty='easy')


1.  I want to tweak __str__ so that it looks like this when printed::

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


3.  I want to iterate through keys and test if a key is inside::

        >>> sorted(list(t))
        ['difficulty', 'importance', 'title']

        >>> 'fibityfoo' in t
        False


4.  Finally, I want to take advantage of pep 3119 and make it easy for
    other people to test if my object is an instance of
    collections.Mapping::

        >>> import collections
        >>> isinstance(t, collections.Mapping)
        True


A few tests
===========

Since I knew exactly what behavior I needed, I wrote a file test_task.py
that tries to run






First I used UserDict
=====================

The UserDict class in the UserDict module

