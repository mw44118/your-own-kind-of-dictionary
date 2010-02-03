++++++++++++++++++++
Listings for article
++++++++++++++++++++


listing1.py
===========

1.  Write a test to verify that our Task class converts to a string
    correctly.  Write a test method that has an error in it.

2.  Write a test that does the same test, but that test should FAIL, not
    hit an ERROR.

3.  Write a first version of the Task class.

4.  Write a test that uses our Task class.  All the tests in should
    pass.

5.  Write second version of the Task class with a less-insane __str__
    method.

6.  Write a test that works on the second version of the Task class.
    All those tests should pass.


listing2.py
===========

1.  Somehow import or copy in the last test written in listing1.py.

2.  Write a test that verifies we can restrict values for keys to a
    set of possible values.

3.  Write another version of Task that passes that test AND the test on
    __str__ from listing1.py.

4.  Write a test verifies we can restrict the values for keys to
    instances of certain types.

5.  Write another version of Task that passes the "allowed types" test.

6.  Write a test that verifies our custom __setitem__ method is used in
    related dictionary functions, like update, setdefault, and during
    __init__.   This test should fail.


listing3.py
===========

1.  Somehow import or copy all the tests from listing2.py.

2.  Write a new Task class that doesn't subclass dictionary.  Use
    composition rather than inheritance, i.e., just use a secret self._d
    attribute.  Then write lots and lots of proxy methods.

3.  Write a new test for lots of related dictionary behaviors and
    methods, like iterating through keys, testing for membership, all
    the nice methods like .keys(), .values(), .items(), .iteritems(),
    etc.

4.  Write a new Task class that implements these methods.

listing4.py
===========

1.  Somehow import or copy all the tests from listing3.py.

2.  Create a new Task class by subclassing UserDict.UserDict.  This
    class should pass all the tests in listing3.py.

3.  Now write a test that requires our Task class to use the super
    method.  This test should raise an ERROR since UserDict.UserDict is
    not a new-style class.

4.  Now write a class inherits from both UserDict.DictMixin and the
    object class.  This class should pass all the tests written so far.

5.  Write a test that checks if our class is a subclass of
    the MutableMapping class.

listing5.py
===========

1.  Somehow import or copy all the tests from listing4.py.

2.  Rewrite the Task class to inherit from UserDict.DictMixin and
    collections.MutableMapping, so that the last test passes.









