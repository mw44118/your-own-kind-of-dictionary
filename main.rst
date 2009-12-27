+++++++++++++++++++++++++++
Your own kind of dictionary
+++++++++++++++++++++++++++

What I need
===========

What I need the object for

What I need the object to do

Possible ways to build it
=========================

I'll use tests to, err, test the different ways to build it
===========================================================

Write a really simple test

Run the test

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
