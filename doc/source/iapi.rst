======================
Internal API reference
======================

.. currentmodule:: pyexcel.iterators
.. _iapi:

This is intended for developers and hackers of pyexcel

Data sheet representation
=========================

In inheritance order from parent to child

.. currentmodule:: pyexcel.iterators
.. autosummary::
   :toctree: iapi/

   Matrix
   
.. currentmodule:: pyexcel.sheets
.. autosummary::
   :toctree: iapi/

   PlainSheet
   MultipleFilterableSheet
   IndexSheet
   Sheet


File type handlers
==================

New file type handlers are registered via two internal static dictionaries: READERS for file readers, and WRITERS for file writers

.. currentmodule:: pyexcel.io
.. autosummary::
   :toctree: iapi/

   load_file
   get_writer