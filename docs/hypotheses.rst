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

.. _extending:

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

Mean word length (in characters)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: translationese.mean_word_length
   :members:

Syllable ratio
^^^^^^^^^^^^^^

.. automodule:: translationese.syllable_ratio
   :members:

Lexical density
^^^^^^^^^^^^^^^

.. automodule:: translationese.lexical_density
   :members:

Mean sentence length
^^^^^^^^^^^^^^^^^^^^

.. automodule:: translationese.mean_sentence_length
   :members:

Mean word rank
^^^^^^^^^^^^^^

.. automodule:: translationese.mean_word_rank
   :members:

Most frequent words
^^^^^^^^^^^^^^^^^^^

.. automodule:: translationese.most_frequent_words
   :members:

N most frequent words in the corpus.

Explicitation
-------------

The tendency to spell out in the target text utterances that are more implicit
in the source.

Explicit naming
^^^^^^^^^^^^^^^

.. automodule:: translationese.explicit_naming
   :members:

Single naming
^^^^^^^^^^^^^

.. automodule:: translationese.single_naming
   :members:

Mean multiple naming
^^^^^^^^^^^^^^^^^^^^

.. automodule:: translationese.mean_multiple_naming
   :members:

Cohesive markers
^^^^^^^^^^^^^^^^

.. automodule:: translationese.cohesive_markers
   :members:

Normalization
-------------

Translators take great efforts to standardize texts.  We include in this the
tendency to avoid repetitions, the tendency to use a more formal style
manifested in refraining from the use of contractions, and the tendency to
overuse fixed expressions even when the source text refrains, sometime
deliberately, from doing so.

Repetitions
^^^^^^^^^^^

.. automodule:: translationese.repetitions
   :members:

Contractions
^^^^^^^^^^^^

.. automodule:: translationese.contractions
   :members:

Average PMI
^^^^^^^^^^^

.. automodule:: translationese.average_pmi
   :members:

Threshold PMI
^^^^^^^^^^^^^

.. automodule:: translationese.threshold_pmi
   :members:

Interference
------------

Associated with the output of non-native speakers producing utterances in their
second language. Operates on different levels from transcribing source language
words, through using loan translations, to exerting structural influence.

POS `n`-grams
^^^^^^^^^^^^^

.. automodule:: translationese.pos_n_grams
   :members:

Character `n`-grams
^^^^^^^^^^^^^^^^^^^

.. automodule:: translationese.character_n_grams
   :members:

Contextual function words
^^^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: translationese.contextual_function_words
   :members:

Positional token frequency
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: translationese.positional_token_frequency
   :members:

Miscellaneous
-------------

A number of features that cannot be associated with any above hypothesis
category.

Function words
^^^^^^^^^^^^^^

.. automodule:: translationese.function_words
   :members:

Pronouns
^^^^^^^^

.. automodule:: translationese.pronouns
   :members:

Punctuation
^^^^^^^^^^^

.. automodule:: translationese.punctuation
   :members:

Ratio of passive forms to all verbs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: translationese.ratio_to_passive_verbs
   :members:
