++++++++++++++++
How to run tests
++++++++++++++++

Run all tests on a single class::

    >>> import unittest
    >>> class Test1(unittest.TestCase):
    ...     def test_1(self):
    ...         assert True
    ...     def test_2(self):
    ...         assert True
    >>> tl = unittest.TestLoader()
    >>> ts = tl.loadTestsFromTestCase(Test1)
    >>> tr = ts.run(unittest.TestResult())
    >>> tr
    <unittest.TestResult run=2 errors=0 failures=0>


Run just one test on a class with several test methods::

    >>> import unittest
    >>> class Test2(unittest.TestCase):
    ...     def test_1(self):
    ...         assert True
    ...     def test_2(self):
    ...         assert True
    ...     def test_3(self):
    ...         assert False
    >>> ts = unittest.TestSuite()
    >>> ts.addTest(Test2('test_1'))
    >>> tr = ts.run(unittest.TestResult())
    >>> tr
    <unittest.TestResult run=1 errors=0 failures=0>
