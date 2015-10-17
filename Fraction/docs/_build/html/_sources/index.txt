.. Fraction documentation master file, created by
   sphinx-quickstart on Fri Oct 16 22:42:23 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Fraction's documentation!
====================================

Fraction is a simple training project for representing fraction in some notation. Fraction is represented by it's
decimal integer numerator and decimal integer denominator. Notation base is also given as decimal integer value.

Fraction API is represented by the class :py:class:`fraction.Fraction`, which stores fraction and performs
representation. It is computed by `fraction.Fraction` main method :py:meth:`fraction.Fraction.represent()`, that
prints representation to the console. Each character of fraction in given notation looks like `#<val>`,
where `<val>` is digit in given notation.


Fraction API:
=============

.. automodule:: fraction
   :members:
   :private-members:

 
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

