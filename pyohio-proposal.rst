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
implementations I tried.  I'll point out where each ultimately failed in
some corner case, until the final solution.  I'll also point out some
stuff that I learned:

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

*   Describe what kind of object I want

*   Discuss the tests written for the first set of features

*   Discuss the first implementation (subclass dict directly) and point
    out why it is inadequate

*   Discuss the second implementation (use composition) and point out
    where it breaks down

*   Discuss third implementation (UserDict.UserDict)

*   Discuss fourth implementation (UserDict.DictMixin)

*   Discuss what the heck PEP 3119 is all about and why it is nice

*   Discuss the last implementation based on collections.MutableMapping



Bio
---

Dad, programmer, gardener, entrepeneur, internet crackpot.  Would love
to do some consulting gigs and is willing to work for $$$.  But the
work must be interesting.

Recording release
-----------------

I will sign the recording release agreement (text at http://wiki.python.org/moin/PyOhio/RecordingRelease).

.. Email to to cfp@pyohio.org by May 10, 2010
