++++++++++++++++++++++++++++++++++++
Building your own kind of dictionary
++++++++++++++++++++++++++++++++++++

.. contents::

What kind of object I want
==========================

It should act like a regular dictionary, except:

*   Change how it prints out (__str__)
*   Allow instances to restrict values for keys (__setitem__)

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
