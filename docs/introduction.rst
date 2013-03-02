Introduction
=============
The project addresses the difference between translated and original non-translated articles. Those differences, also refered as 'Features' have been discussed and studied in the last three decades. In this project, we wish to quantify this differences. 

It is not trivial to differ between the two group from the look of the naked eye. In order to successed in distinguishing, We use machine learning and classification methods. The classification is done based on these features, estimated during texts analysis. These mentioned features are also refered as 'attributes'.  

For many years, it has been suggested that there are differences between originaly English texts and translated ones. 
For example, it has been suggested that translated texts have a narrow vocabulary use. Meaning, the number of different words used is smaller among translated text compared to original texts. 

Many tried to find the correct and appropriate attributes that will maximize the classification results. In this work, we use all attributes in the classification, to assure a correct separation and minimization of the classification error.


This project is based on 'On The Features Of Translationese' article, written by V. Volansky, N. Ordan and S. Wintner. Our work implements the attributes presented in the article and classify according to this attributes. The analysis was conducted on EUROPARL corpus texts.  

The Attributes are grouped into 5 hypothese categories:
        1. Simplification - refers to the process of rendering complex linguistic features in the source text into simpler features in the target text.
          
        2. Explicitation - refers to the tendency to spell out in the target text utterances that are more implicit in the source.

        3. Normalization - refers to the tendency to avoid repetitions, the tendancy to use more formal style, the tendency to overuse fixed expressions even when the source text refrains.

        4. Interference  - associated with the output of non-native speakers producing utterances in their second language. Operates on different levels from transcribing source language words, through using loan translations, to exerting structual influence.

        5. Miscellaneous - number of features that cannot be associated with any above hypothese.

For more information and details about the attributes nature, navigate to the 'Attributes Documentation' page. 
