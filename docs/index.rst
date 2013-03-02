.. translationese documentation master file, created by
   sphinx-quickstart on Sun Feb 24 00:18:00 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Analysis of Translationese
==========================

.. toctree::
   :maxdepth: 2

   introduction
   hypotheses
   utils
   testing

This project analyzes the various features attributed to a language known as
`translationese`.  The project was developed in the Natural Language Processing
Laboratory, under the supervision of Prof. Shuly Wintner.

Project description
-------------------

The project's goal is distinguishing between texts that were originally written
in English ("`O`" texts) and texts written in foreign languages and were
translated into English ("`T`" texts). This is done based on features and
characteristics found within the texts.

Getting started
---------------

For basic usage, place several originally-english (`O`) files in
``/home/user/original``, and several translated-to-english (`T`) files in
``/home/user/translated``. Now, run the following:

.. code-block:: bash

    $ ./analyze.py -o ~/original -t ~/translated -v 0 lexical_variety
    $ weka lexical_variety_0.arff
    # Or, for immediate textual results:
    $ weka -c weka.classifiers.functions.SMO -- -t lexical_variety_0.arff

This will run the :mod:`lexical_variety` quantifier, using variant 0, and
run WEKA's SMO classifier-builder on the output.

Tools used
----------

Python 2.7
    Code for processing, analyzing and self-testing. http://python.org
NLTK Library
    Natural Language ToolKit for python. Text processing and analysis was
    performed using this library. http://nltk.org
Weka 3.7
    Classification tool. Uses ARFF files as input.
    http://www.cs.waikato.ac.nz/ml/weka/
Sphinx
    Documentation generator.
    http://sphinx-doc.org

We would like to thank our guide, Prof. Shuly Wintner.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
