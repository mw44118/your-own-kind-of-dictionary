+++++++++++++++++++++++++++++++++++++++++++++++
Proposal: how to properly subclass dictionaries
+++++++++++++++++++++++++++++++++++++++++++++++


I'd like to write a short article describing experience adding
dictionary features to a class.

Background
==========

I needed an object like the regular dictionary, but I wanted to alter
how __str__ worked, and I wanted to restrict allowed values for some
keys, by altering how __setitem__ works.

This was messier than it should have been:

1.  subclassing dict was no good because methods like update and
    setdefault wouldn't use my __setitem__ method.

2. The UserDict.UserDict class is not a new-style class, so any
    sub-subclass (grandchild class?) couldn't use super, so this was out.

3.  The UserDict.DictMixin is OK until you use python 2.6.

4.  As of python 2.6, the collections module has a MutableMapping class
    which is recommended instead of UserDict.DictMixin.  The
    collections.MutableMapping does everything UserDict.DictMixin does
    AND it has the nice benefit of inheriting from the abstract base class
    Mapping.


Outline
=======

1.  In TDD fashion, write out some unittest.TestCase classes for all the
    features I want in my class.

2.  Go through the different approaches I listed above until I get to
    collections.MutableMapping.

3.  Spend a few sentences explaining what is so great about using
    abstract base classes vs. doing duck typing by calling methods and
    then catching exceptions.
