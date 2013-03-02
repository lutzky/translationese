Attributes Documentation
========================
This page will describe the meaning of an attribute and an implementation asspects of an attribute.


What is an attribute?
---------------------
Attributes (also named features) are hypothesis known among the natural langugae processing community. Based on hypothesis the seperation between translated and non-translated texts is capable. Each attributes refers to different characteristic in a text and can be quantified.

A simple example for such attribute, is based on the hypothsis in which translated texts contains more repetitions, therefore the amount of different words within the text is smaller compared to non-translated texts. These is based on the assumption that the writter of a translated texts would probably have more narrow vocabulary than a native writter. 

The attribute quantify this hypothesis by counting the amount of different words given a text. The estimation is expected to be decreased for translated texts.

Asspects of Implementation
--------------------------
Each attributes was implemented, tested and resulted seperately. The attributes operates an helper funcations, provided by the Analysis class, for analyzing the texts. For example, using NLTK, one of the Analysis function provides a convertion from texts to tokens list. 

Each attribute must implement a 'QUANTIFY' function. The quantify function is operated by the

For variable attributes, an attributes implements an 'VARIABLE'.


List Of Attributes
==================
Simplification
--------------
  * Lexical variety     - original texts are richer in terms of vocabulary.
  * Mean word length    - in characters.
  * Syllable ratio      - translated texts resulting in fewer syllable per word.
  * Lexical density     - frequency of tokens that aren't nouns, adjective, adverbs and verbs.
  * Mean sentence length
  * Mean word length    - less frequent words are used more often in original texts.
  * Most frequent words - N most frequent words in the corpus.

Explicitation
-------------
  * Explicit naming      - the use of a personal pronoun as a clarification of a proper noun.
  * Single naming
  * Mean multiple naming - average length in tokens of proper nouns.
  * Cohesive markers     - translation texts known to use more cohesive markers. pointed 40 markers in list.

Normalization
-------------
  * Repetitions         - number of content words that occure more than once in a chunck.
  * Contractions        - ratio of contracted forms to their counterpart full forms.
  * Average PMI         - original texts use more collocations.
  * Threshold PMI

Interference
------------
  * POS n-grams         - actual number of each POS n-grams in a chunck.
  * Character n-grams   
  * Contextual function words
  * Positional tokens frequency - frequency of tokens in the first, second, antepenultimate, penultimate and last positions.

Miscellaneous
-------------
  * Function words         - frequency of occurence of each function words from pre-defined list.
  * Pronoun                - frequency of occurence of each pronoun from pre-defined list.
  * Punctuation            - frequency of each puncuation mark in the chunck.
  * Ratio of passive verbs - original texts tend to use passive form of verbs more than translated texts. 

