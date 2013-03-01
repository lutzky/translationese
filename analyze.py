#!/usr/bin/python

"""analyze.py

Run an analysis of a directory of non-translated ("O") and
translated ("T") files. Analysis will be performed based on
selected properties and output to stdout in ARFF format, suitable
for use with weka."""

import os
import sys
import translationese
import time
import pkgutil
import logging
from translationese import MissingVariant
import StringIO

class Timer:
    """Simple progress reporter. Call ``increment`` for every event
    which occurs, and every ``report_every`` seconds the count and
    average time will be displayed."""

    def __init__(self, report_every=10, stream=sys.stderr):
        self.report_every = report_every
        self.stream = stream

        self.started_at = 0
        self.count = 0
        self.prevtime = 0

    def start(self):
        """[re-]start the timer"""
        self.started_at = time.time()
        self.prevtime = self.started_at
        self.count = 0

    def increment(self):
        """Report an event as having occured."""
        self.count += 1
        if time.time() - self.prevtime > 1:
            elapsed = time.time() - self.started_at
            average_ms = 1000.0 * (elapsed / self.count)
            self.stream.write(\
                    "\r[%5d] %d seconds elapsed, (%.2f ms each)" \
                    % (self.count, elapsed, average_ms))
            self.prevtime = time.time()

    def stop(self):
        """Stop the timer, properly formatting end-of-line."""
        self.stream.write("\n")

def analyze_file(filename, analyzer_module, variant=None):
    with translationese.Analysis(filename=filename) as analysis:
        if variant is not None:
            return analyzer_module.quantify_variant(analysis, variant)
        else:
            return analyzer_module.quantify(analysis)

def analyze_directory(dir_to_analyze, expected_class, analyzer_module,
                      variant=None, timer=None):
    results = []

    for filename in sorted(os.listdir(dir_to_analyze)):
        if filename.endswith(".analysis"):
            # This is a cached analysis, skip it.
            continue
        filename = os.path.join(dir_to_analyze, filename)
        try:
            result = analyze_file(filename, analyzer_module, variant)
            if timer: timer.increment()
        except:
            logging.error("Error analyzing file %s", filename)
            raise

        results.append((result, expected_class))

    return results

def print_results(results, stream):
    attributes = set()

    print >> stream, "@relation translationese"

    for result, _ in results:
        attributes.update(result.keys())

    attributes = list(attributes)
    attributes.sort()

    for attribute in attributes:
        print >> stream, "@attribute %s numeric" % repr(attribute)

    # Class attribute should be last, as this is the weka default.
    print >> stream, "@attribute class { T, O }"
    print >> stream
    print >> stream, "@data"

    for result, expected_class in results:
        line = ",".join([str(result.get(x, 0)) for x in attributes])

        print >> stream, "%s,%s" % (line, expected_class)

def main(analyzer_module, o_dir, t_dir, stream=sys.stdout, variant=None):
    """Internal, testable main() function for analysis."""
    if variant is None:
        if not hasattr(analyzer_module, "quantify"):
            raise MissingVariant("%s requires a variant to be specified" % \
                                 analyzer_module.__name__)
    elif not hasattr(analyzer_module, "quantify_variant"):
        raise translationese.NoVariants("%s does not support variants" % \
                                        analyzer_module.__name__)

    timer = Timer()
    results = []

    logging.info("Analyzing 'O' directory %s", o_dir)
    timer.start()
    results += analyze_directory(o_dir, "O", analyzer_module, variant, timer)
    timer.stop()

    logging.info("Analyzing 'T' directory %s", t_dir)
    timer.start()
    results += analyze_directory(t_dir, "T", analyzer_module, variant, timer)
    timer.stop()

    logging.info("Writing results")
    timer.start()
    print_results(results, stream)
    timer.stop()

def import_translationese_module(module_name):
    return __import__('translationese.%s' % module_name,
                      fromlist='translationese')

def valid_translationese_module(module):
    if hasattr(module, 'quantify'):
        return True
    if hasattr(module, 'quantify_variant'):
        return True
    return False

def format_columns(l):
    """Format a list into two columns.

    >>> print format_columns(["111", "12", "1234", "124", "12"])
    111  124
    12   12
    1234
    """
    first_column_length = (len(l) + 1) / 2
    column_a = l[:first_column_length]
    column_b = l[first_column_length:]
    width = max([len(s) for s in column_a])

    if len(column_a) > len(column_b):
        column_b.append("")

    s = StringIO.StringIO()

    for i in range(len(column_a)):
        print >> s, column_a[i].ljust(width), column_b[i]

    return s.getvalue().rstrip()

def available_modules():
    iterator = pkgutil.iter_modules(['translationese'])
    module_names = list(x[1] for x in iterator
                        if valid_translationese_module(
                           import_translationese_module(x[1])
                         ))

    return format_columns(module_names)

def get_output_stream(outfile, variant, module_name):
    if not outfile:
        if variant is None:
            outfile = "%s.arff" % module_name
        else:
            outfile = "%s_%d.arff" % (module_name, variant)

    outstream = open(outfile, "w")

    return outstream

def cmdline_main():
    """External main() function for calling from commandline."""
    from optparse import OptionParser

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)-15s [%(levelname)-6s] %(message)s')

    usage = "%%prog [options] MODULE\n\n" \
            "Available modules:\n%s" % available_modules()

    parser = OptionParser(usage=usage)
    parser.add_option("-v", "--variant", dest="variant", default=None,
                      type="int", help="Variant for analysis module")
    parser.add_option("-t", dest="t_dir", default='./t/',
                      help="Directory of T (translated) texts " \
                           "[default: %default]")
    parser.add_option("-o", dest="o_dir", default='./o/',
                      help="Directory of O (original) texts " \
                           "[default: %default]")
    parser.add_option("--outfile", dest="outfile",
                      help="Write output to OUTFILE.\n" \
                           "[default: MODULE[_VARIANT].arff]")

    options, args = parser.parse_args()

    try:
        module_name = args[0]
        module = import_translationese_module(module_name)
    except IndexError:
        parser.error("No MODULE specified")
    except Exception, ex:
        parser.error(ex)

    for dir_path in options.t_dir, options.o_dir:
        if not os.path.isdir(dir_path):
            parser.error("No such directory %r (run with --help)" % dir_path)

    outfile = get_output_stream(options.outfile, options.variant, \
                                module_name)

    logging.info("Output will be written to %s", outfile)
    main(module, o_dir=options.o_dir, t_dir=options.t_dir,
         variant=options.variant, stream=outfile)

if __name__ == '__main__':
    cmdline_main()
