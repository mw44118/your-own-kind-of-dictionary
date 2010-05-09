Building your own kind of dictionary by writing tests
=====================================================

:Type: talk

:Presenter: W. Matthew Wilson <matt@tplus1.com>

:Python level: intermediate

Description
-----------

I wanted an object like the regular python dictionary, but with a few
small tweaks:

*   Tweak the __str__ method
*   Restrict values for some keys to elements of a set
*   Restrict values for some keys to instances of a type

This sounds trivial, but it ain't.

In the talk, I'll walk through the tests I wrote and the different
implementations I tried until coming up with a winner.  I'll also point
out some stuff that I learned:

*   Subclassing types defined in C doesn't do what I thought it would
    do.

*   UserDict.UserDict in the standard library is not a new-style class!

*   PEP 3119 is a nifty solution to a few problems with duck-typing.  It
    is more difficult than it should be to distinguish between a
    dictionary and a list.

Extended description
--------------------

You can read all the code and tests and the talk itself online at my
github repository at
http://github.com/mw44118/your-own-kind-of-dictionary.


Outline
-------

I'm not done, but this is the skeleton I'll likely follow:

*   What kind of object I want (described using tests)

*   Walk through first implementation (subclass dict) and test results

*   composition-based approach

*   UserDict.UserDict

*   UserDict.DictMixin

*   PEP 3119 and why it is nice

*   collections.MutableMapping


Bio
---

Dad, programmer, gardener, entrepeneur, internet crackpot.  Blogs at
http://blog.tplus1.com.

Recording release
-----------------

I will sign the recording release agreement (text at http://wiki.python.org/moin/PyOhio/RecordingRelease).

.. Email to to cfp@pyohio.org by May 10, 2010
