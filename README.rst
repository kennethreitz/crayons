Crayons: Text UI colors for Python.
===================================

This module is really simple, it gives you colored strings for terminal
usage. Included colors are ``red``, ``green``, ``yellow``, ``blue``, ``black``, ``magenta``, ``cyan``, and ``white``, ( as well as ``clean`` and ``disable``).

**Crayons** is nice because it automatically wraps a given string in both the foreground color, as well as returning to the original state after the string is complete. Most terminal color libraries make you manage this yourself. 

Arguments in include ``always=True`` and ``bold=True``. 

Features
--------

- If you call ``disable()``, all future calls to colors will be ignored.
- If the current process is not in a TTY (e.g. being piped), no colors will be displayed.
- Length of ColoredStrings can be properly calculated.
- Powered by colorama.

Usage is simple
---------------

::

    # red is red, white is white.
    >>> print '{} white'.format(crayons.red('red'))
    red white

That's it!

Installation
------------

::

    $ pip install crayons
