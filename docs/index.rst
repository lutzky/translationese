.. translationese documentation master file, created by
   sphinx-quickstart on Sun Feb 24 00:18:00 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Analysis of Translationese
==========================

This project analyzes the various features attributed to a language known as
`translationese`.  The project was developed in the Natural Language Processing
Laboratory, under the supervision of Prof. Shuly Wintner.

Project description
-------------------

The project's goal is distinguishing between texts that were originally written
in English ("`O`" texts) and texts written in foreign languages and were
translated into English ("`T`" texts). This is done based on features and
characteristics found within the texts.

Tools used
----------

Python 2.7
    Code for processing, analyzing and self-testing.
NLTK Library
    Natural Language ToolKit for python. Text processing and analysis was
    performed using this library.
Weka 3.7
    Classification tool. Uses ARFF files as input.
Sphinx
    Documentation generator.

We want to thank our guide, Prof. Shuly Wintner.

.. toctree::
   :maxdepth: 2

   introduction
   attributes
   code
        
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
