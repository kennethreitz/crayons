Crayons: Text UI colors for Python.
===================================

This module is really simple, it gives you colored strings for terminal
usage. Included colors are ``red``, ``green``, ``yellow``, ``blue``, ``black``, ``magenta``, ``magenta``, ``cyan``, ``white``, ``clean``, and ``disable``.

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
    >>> print '{red} white'.format(red=crayons.red('red'))
    red white

That's it!

Installation
------------

::

    $ pip install crayons
