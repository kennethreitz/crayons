Crayons: Text UI colors for Python.
===================================

.. image:: https://img.shields.io/pypi/v/crayons.svg
    :target: https://pypi.python.org/pypi/crayons

.. image:: https://img.shields.io/pypi/l/crayons.svg
    :target: https://pypi.python.org/pypi/crayons

.. image:: https://img.shields.io/pypi/wheel/crayons.svg
    :target: https://pypi.python.org/pypi/crayons

.. image:: https://img.shields.io/pypi/pyversions/crayons.svg
    :target: https://pypi.python.org/pypi/crayons

.. image:: https://img.shields.io/badge/SayThanks.io-☼-1EAEDB.svg
    :target: https://saythanks.io/to/kennethreitz



This module is really simple, it gives you colored strings for terminal
usage. Included colors are ``red``, ``green``, ``yellow``, ``blue``, ``black``, ``magenta``, ``cyan``, ``white``, and ``normal`` ( as well as ``clean`` and ``disable``).

**Crayons** is nice because it automatically wraps a given string in both the foreground color, as well as returning to the original state after the string is complete. Most terminal color libraries make you manage this yourself. 


.. image:: https://d3vv6lp55qjaqc.cloudfront.net/items/3q0I293q1z293R3a3a3n/Screen%20Shot%202017-01-23%20at%206.00.02%20PM.png?X-CloudApp-Visitor-Id=2577


Arguments include ``always=True`` and ``bold=True``. 

Features
--------

- If you call ``disable()``, all future calls to colors will be ignored.
- If you call ``normal()``, color is reset to default foreground color
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
