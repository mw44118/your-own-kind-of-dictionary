Building your own kind of dictionary
====================================

:Type: talk

:Presenter: W. Matthew Wilson <matt@tplus1.com>

:Python level: novice

Description
-----------

My talk is based on a project that seemed very simple at first.  I
wanted an object like the regular python dictionary, but with a few
small tweaks:

*   values for some keys should be restricted to elements of a set
*   values for some keys should be restricted to instances of a type

For example, pretend I want a dictionary called favorites, and I want
the value for the "color" key to be any instance of my Color class.
Meanwhile, for the "movie" key, I want to make sure that the value
belongs to my set of movies.

In the talk, I'll walk through how I used tests to validate my different
implementations until I came up with a winner.

Unlike my talk last year on metaclass tomfoolery, and the year before
that on fun with decorators (and decorator factories) I'm hoping to make
this talk straightforward and friendly to beginning programmers.

You'll see:

*   how I use tests to solve a real-world problem
*   a few little gotchas with the super keyword
*   a little about how python works under the hood.

Extended description
--------------------

I'm not done with the slides, but all my code examples are finished.
You can read it all online at my github repository `here`_.

.. _here: at http://github.com/mw44118/your-own-kind-of-dictionary

Outline
-------

*   What kind of object I want
    *   Tests define the expected behavior
    *   How to run those tests

*   First implementation (subclass dict)
    *   How the implementation is defined
    *   Examine test results
    *   Examine the C code behind the dict class to see why my
        subclassed __setitem__ method won't get called from the parent
        class

*   Composition-based implementation
    *   Explain the composition approach vs inheritance
    *   Examine test results
    *   Point out irritating to either manually redefine every
        related dictionary method on the container class
    *   Show how to use __getattr__ to avoid all that boring wrapper
        code
    *   Show how __getattr__ doesn't play nice with inspection tools

*   UserDict.UserDict
    *   Explain implementation
    *   Examine test results
    *   Add a new test that uses this class as a parent for a subclass
    *   Explain how UserDict.UserDict is not a new-style class, so the
        super keyword fails.

*   UserDict.DictMixin
    *   Explain implementation
    *   Examine test results

*   PEP 3119 and why it is nice
    *   duck-typing, why it is awesome, why it isn't perfect
    *   abstract base classes
    *   As of python 2.6, don't use UserDict.DictMixin; use
        collections.MutableMapping


Bio
---

Dad, programmer, gardener, entrepeneur, internet crackpot.  Blogs at
http://blog.tplus1.com.

Recording release
-----------------

I will sign the recording release agreement (text at
http://wiki.python.org/moin/PyOhio/RecordingRelease).

.. Email to to cfp@pyohio.org by May 10, 2010
