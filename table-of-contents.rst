+++++++++++++++++++++++++++
Your own kind of dictionary
+++++++++++++++++++++++++++

What I need the object for

What I need the object to do

Possible ways to build it

I'll use tests to test the different ways to build it.

Write a trivial test that stores something in our dictionary and gets it
out.

Run the test on our nonexistent object.

Subclass dict

Run test on the dict subclass

Now add a test to use the update method.

Run both tests and see what happens.

Discuss how dict subclasses won't use my __setitem__ method in related
methods.

Just build up a dictionary-like object by writing all the methods from
scratch

Subclass test classes so that they use an instance of the from-scratch
class.

Show how to run just a single test class rather than all of them.

Run tests on from-scratch class.

Write a test to use the setdefault method, run it, then extend the code.

Write a test to iterate through keys, run it, and then extend the code.

Discuss that there should be an easier way rather than building up
EVERYTHING from scratch.

Subclass UserDict.UserDict

Run existing tests on UserDict.UserDict

Subclass UserDict.DictMixin

Run tests on UserDict.DictMixin

What about abstract base classes

Write a test to see if my class is an instance of collections.Mapping
subclass.

Now subclass collections.MutableMapping and rerun our tests.

And we're done!
