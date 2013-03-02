Introduction
============

The project addresses the difference between translated and original
non-translated texts. Those differences, also referred as `features` or
`attributes`, have been discussed and studied in the last three decades. In
this project, we wish to quantify these differences. 

For a human, it is not trivial to differentiate between the two groups. In
order to successfully distinguish between them, we use machine learning and
classification methods. The classification is done based on these features,
estimated during texts analysis.

For many years, it has been suggested that there are differences between
originally English texts and translated ones.  For example, it has been
suggested that translated texts have a narrow vocabulary use. Therefore, the
number of different words used is smaller among translated text compared to
original texts. (See :py:module:`lexical_variety`).

Many tried to find the correct and appropriate attributes that will maximize
the classification results. In this work, we try each of these attributes,
attempting to analyze which ones provide the best separation.

This project is based on `On The Features Of Translationese` article, written
by V. Volansky, N. Ordan and S. Wintner. Our work implements the attributes
presented in the article and classifies texts according to them. The analysis
was conducted on EUROPARL corpus texts.  

The Attributes are grouped into 5 hypothesis categories:

Simplification
        The process of rendering complex linguistic features in the
        source text into simpler features in the target text.
Explicitation
        The tendency to spell out in the target text utterances that are more
        implicit in the source.
Normalization
        The tendency to avoid repetitions, use more formal style, and overuse
        fixed expressions even when the source text refrains.
Interference
        Associated with the output of non-native speakers producing utterances
        in their second language. Operates on different levels from
        transcribing source language words, through using loan translations, to
        exerting structural influence.
Miscellaneous
        A number of features that cannot be associated with any above
        hypothesis category.

For more information and details about the attributes nature, navigate to the
:ref:`attributes` page.
