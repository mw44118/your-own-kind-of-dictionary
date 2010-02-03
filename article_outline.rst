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

    *   TestRestrictToSets verifies I can set a key to a regular value.

    
    *   TestRestrictToTypes

    *   


*   Discuss listing3

*   Discuss listing4

*   Discuss listing5

*   Discuss listing6

*   Summary
