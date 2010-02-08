+++++++++++++++++++++++++++++++++++++++
Outline for Your Own Kind of Dictionary
+++++++++++++++++++++++++++++++++++++++

*   What I want

*   Why I want a dictionary

*   What do I need my object to do

    *   Tweak the __str__ method
    *   Restrict values for some keys
    *   quack like a dictionary

*   I'll use something vaguely similar to TDD

*   Discuss listing1

    *   TestTaskAsString.test_as_str_when_empty verifies the task prints right when empty.
    *   TestTaskAsString.test_as_str_with_data verifies the str method when keys exist.
    *   Point out how self.Task ain't defined in TestTaskAsString1, so
        these tests are going to crash.

    *   The BogusTask class won't do anything, but our tests won't crash
        with errors.

    *   TestBogusTaskAsString uses the BogusTask class.  The important thing to
        understand here is the difference between tests with errors in
        them and tests that fail.  These tests will fail because the
        assert statements will raise AssertionErrors.

    *   The UglyTask class has a custom __str__ method.

    *   TestAsString3 tests if UglyTask does stuff right.

    *   RefactoredTask has a prettier __str__ method.

    *   TestRefactoredTaskAsString verifies we didn't break anything
        when we rewrote UglyTask into RefactoredTask.

*   Discuss listing2

    *   I import listing1 so I can rerun the tests and extend
        RefactoredTask I worked on.

    *   I copy in the first __str__ method so that I can pass the
        TaskAsString test.

    *   TestRestrictToSets verifies I can limit values for a key to a
        set.

    *   TestRestrictToTypes does a similar test, but for types.

    *   TestRestrictToTypes also tests that initializing a Task with
        invalid types fails.

    *   TestRestrictToTypes tests that the dictionary method update
        uses our special __setitem__.

    *   Point out that these two tests (__init__ and update) both fail.


*   Discuss listing3

    *   Instead of inheriting from dict, I embed a dictionary instance
        as an attribute.

    *   I define the methods required to make my object act like
        dictionary.

    *   I define keys() and values() by just returning the results of
        calling the exact same method on self.d.

    *   There is a pattern in the keys and the values method.

    *   I use __getattr__ to methods directly to the inner
        dictionary instance attribute.

    *   Using __getattr__ means that as new methods and attributes are
        added to the main dict class, my Task will handle them
        correctly.

    *   On the downside, it isn't straightforward to inspect an instance
        from the outside and see what methods it exports.

    *   I define methods like update manually and make sure they call my
        special __setitem__ method.  If I just let __getattr__ handle
        them, then self._d will use its own update method, and that one
        will not use my __setitem__.


*   Discuss listing4

    *   Use the UserDict.UserDict class.

    *   UserDict.UserDict doesn't allow iteration across keys.

    *   UserDict.UserDict is not a new-style class, i.e., it doesn't
        inherit from object.  That means that you can't use super with
        it to call parent class methods.


*   Discuss listing5

    *   Use the UserDict.DictMixin.

    *   I define __getitem__, __setitem__, __delitem__, and keys, and
        the mixin does the rest.

    *   Since I subclass both object and UserDict.DictMixin, I don't
        have the same problem with using super.

*   Discuss listing6

*   Summary
