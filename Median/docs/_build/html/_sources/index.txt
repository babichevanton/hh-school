.. Median documentation master file, created by
   sphinx-quickstart on Fri Oct 16 14:29:13 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Median's documentation!
==================================

Median is a simple training module for finding median of row of numbers. Row is combined from two sorted subrows
that should be taken from console. Each subrow is considered to be sorted in some order row of float numbers. 
In case of error while processing input string system shows error message and offers user to retry input.

Median's API is represented by :py:func:`median_of_row.median()` which takes two sorted rows of numbers and computes
the median of row combined from both taken rows.

Median API:
===========
.. automodule:: median_of_row
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

