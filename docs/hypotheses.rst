.. _hypotheses:

Hypotheses
==========

What is a hypothesis?
---------------------

Each hypothesis describes a set of `attributes` or `features` of a given text.
Specifically, features are chosen in an attempt to distinguish between
translated and non-translated texts. Each attribute refers to different
characteristics of a text and can be quantified.

For example, it is hypothesized that
translated texts contains more repetitions, therefore the amount of different
words within the text is smaller when compared to non-translated texts. This is
based on the assumption that the author of a translated text would probably
have a more narrow vocabulary than a native writer. 

The :mod:`translationese.lexical_variety` module quantifies this hypothesis by
counting the amount of different words in a given text. The value is expected
to be lower for translated texts.

Aspects of Implementation
^^^^^^^^^^^^^^^^^^^^^^^^^

Each hypothesis is implemented and tested and separately, in its own Python
`module`. Such a module can be written quite easily, extending the
functionality of this software. Attributes go in
``translationese/hypothesis_name.py``, and accompanying tests usually go in
``tests/test_hypothesis_name.py``. A simple hypothesis looks like this::

    import translationese

    def quantify(analysis):
        # Hint for Eclipse PyDev autocompletion
        assert isinstance(analysis, translationese.Analysis)

        # ... compute some attributes of the text

        results = {
            "attribute1": 0.5,
            "attribute2": 0.75,
            # ...
            "attributeN": 0.2
        }

        return results

The ``quantify`` method receives a :class:`translationese.Analysis` object.
This facilitates ``pickle``-caching performed by
:class:`translationese.Analysis`.

.. note::

   Attributes can be dynamic, and different every time. The :mod:`analyze`
   module will join all of the attributes (dictionary keys) from the analyses
   of the various texts when producing ARFF output.

Some hypotheses have multiple possible variants. A module for a hypothesis with
variants should look like this::

    import translationese

    VARIANTS = [0, 1, 2, 3] #: Possible variants

    def quantify_variant(analysis, variant):
        # Hint for Eclipse PyDev autocompletion
        assert isinstance(analysis, translationese.Analysis)

        # ... compute some attributes of the text

        results = {
            "attribute1": 0.5,
            "attribute2": 0.75,
            # ...
            "attributeN": 0.2
        }

        return results

A variant is a 0-based integer which can affect the quantification. The
``VARIANTS`` variable is used by the :mod:`analyze` module when given the
``ALL`` parameter - these are the variants which will be used in the complete
analysis, and may be a subset of variants which ``quantify_variant`` will
really accept.

.. note::

   The comment beginning with ``#:`` following ``VARIANTS`` ensures that it
   shows up in the generated documentation.

If expensive text-analysis functions (e.g. :mod:`nltk`) are used in the
quantification, it is recommended that the be moved to the
:class:`translationese.Analysis` class, using :mod:`memoize`, as this will
enable caching.

Simplification
--------------

The process of rendering complex linguistic features in the source text into
simpler features in the target text.

Lexical variety
^^^^^^^^^^^^^^^

.. automodule:: translationese.lexical_variety
   :members:

Mean word length
^^^^^^^^^^^^^^^^

less frequent words are used more often in original texts.


.. automodule:: translationese.mean_word_length
   :members:

Syllable ratio
^^^^^^^^^^^^^^

translated texts resulting in fewer syllable per word.

.. automodule:: translationese.syllable_ratio
   :members:

Lexical density
^^^^^^^^^^^^^^^

frequency of tokens that aren't nouns, adjective, adverbs and verbs.

.. automodule:: translationese.lexical_density
   :members:

Mean sentence length
^^^^^^^^^^^^^^^^^^^^

.. automodule:: translationese.mean_sentence_length
   :members:

Most frequent words
^^^^^^^^^^^^^^^^^^^^

.. automodule:: translationese.most_frequent_words
   :members:

N most frequent words in the corpus.


Explicitation
-------------

The tendency to spell out in the target text utterances that are more implicit
in the source.

  * Explicit naming      - the use of a personal pronoun as a clarification of a proper noun.
  * Single naming
  * Mean multiple naming - average length in tokens of proper nouns.
  * Cohesive markers     - translation texts known to use more cohesive markers. pointed 40 markers in list.

Normalization
-------------
The tendency to avoid repetitions, use more formal style, and overuse fixed
expressions even when the source text refrains.

  * Repetitions         - number of content words that occure more than once in a chunck.
  * Contractions        - ratio of contracted forms to their counterpart full forms.
  * Average PMI         - original texts use more collocations.
  * Threshold PMI

Interference
------------

Associated with the output of non-native speakers producing utterances in their
second language. Operates on different levels from transcribing source language
words, through using loan translations, to exerting structural influence.

  * POS n-grams         - actual number of each POS n-grams in a chunck.
  * Character n-grams   
  * Contextual function words
  * Positional tokens frequency - frequency of tokens in the first, second, antepenultimate, penultimate and last positions.

Miscellaneous
-------------

A number of features that cannot be associated with any above hypothesis
category.

  * Function words         - frequency of occurence of each function words from pre-defined list.
  * Pronoun                - frequency of occurence of each pronoun from pre-defined list.
  * Punctuation            - frequency of each puncuation mark in the chunck.
  * Ratio of passive verbs - original texts tend to use passive form of verbs more than translated texts. 

