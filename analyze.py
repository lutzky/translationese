#!/usr/bin/python

"""analyze.py

Run an analysis of a directory of non-translated ("O") and
translated ("T") files. Analysis will be performed based on
selected properties and output to stdout in ARFF format, suitable
for use with weka."""

import os
import sys
import translationese

AVAILABLE_PROPERTIES = [
                       "average_sentence_length",
                       "mean_word_length",
                       "type_token_ratio",
                       ]

def analyze_file(f, properties):
    analysis = translationese.Analysis(f)
    
    return [ getattr(analysis, prop)() for prop in properties ]

def analyze_directory(dir_to_analyze, expected_class, properties):
    for filename in os.listdir(dir_to_analyze):
        with open(os.path.join(dir_to_analyze, filename)) as f:
            analysis = [expected_class]
            analysis += analyze_file(f, properties)
            print ",".join([str(x) for x in analysis])
        
def main(o_dir, t_dir):
    # TODO: Properties should be selected in command-line.
    properties = AVAILABLE_PROPERTIES
    
    print "@relation translationese"
    print "@attribute class { T, O }"
    
    for prop in properties:
        print "@attribute %s numeric" % prop
    
    print
    print "@data"
    
    analyze_directory(o_dir, "O", properties)
    analyze_directory(t_dir, "T", properties)

if __name__ == '__main__':
    if len(sys.argv) < 3 or \
        not os.path.isdir(sys.argv[1]) or \
        not os.path.isdir(sys.argv[2]):
        print """\
Usage: %s O_DIR T_DIR

    O_DIR   Directory containing non-translated texts
    T_DIR   Directory containing translated texts""" % sys.argv[0]
        sys.exit(1)
    
    main(sys.argv[1], sys.argv[2])