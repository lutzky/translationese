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

class Timer:
    def __init__(self, report_every = 10, stream=sys.stderr):
        self.report_every = report_every
        self.stream = stream

    def start(self):
        self.started_at = time.time()
        self.prevtime = self.started_at
        self.count = 0

    def increment(self):
        self.count += 1
        if time.time() - self.prevtime > 1:
            elapsed = time.time() - self.started_at
            average_ms = 1000.0 * (elapsed / self.count)
            self.stream.write(\
                    "\r[%5d] %d seconds elapsed, (%.2f ms each)" \
                    % (self.count, elapsed, average_ms))
            self.prevtime = time.time()

    def finish(self):
        self.stream.write("\n")

_timer = None

def analyze_file(filename, analyzer_module, variant=None):
    with translationese.Analysis(filename = filename) as analysis:
        if variant is not None:
            return analyzer_module.quantify_variant(analysis, variant)
        else:
            return analyzer_module.quantify(analysis)

def analyze_directory(dir_to_analyze, expected_class, analyzer_module,
                      variant=None):
    attributes = set()
    results = []

    for filename in sorted(os.listdir(dir_to_analyze)):
        if filename.endswith(".analysis"):
            # This is a cached analysis, skip it.
            continue
        filename = os.path.join(dir_to_analyze, filename)
        try:
            result = analyze_file(filename, analyzer_module, variant)
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
        if _timer: _timer.increment()

def main(analyzer_module, o_dir, t_dir, stream=sys.stdout, variant=None):
    if variant is None:
        if not hasattr(analyzer_module, "quantify"):
            raise translationese.MissingVariant("%s requires a variant to be specified" % \
                                                analyzer_module.__name__)
    elif not hasattr(analyzer_module, "quantify_variant"):
        raise translationese.NoVariants("%s does not support variants" % \
                                        analyzer_module.__name__)

    if _timer: _timer.start()

    results = []

    results += analyze_directory(o_dir, "O", analyzer_module, variant)
    results += analyze_directory(t_dir, "T", analyzer_module, variant)

    print_results(results, stream)

def available_modules():
    iterator = pkgutil.iter_modules(['translationese'])
    return ( x[1] for x in iterator )

def get_output_stream(auto_outfile, variant, module_name):
    if auto_outfile:
        if variant is None:
            outfile_name = "%s.arff" % module_name
        else:
            outfile_name = "%s_%d.arff" % (module_name, variant)

        outfile = open(outfile_name, "w")
    else:
        outfile = sys.stdout

    return outfile

def cmdline_main():
    """External main() function for calling from commandline."""
    from optparse import OptionParser

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)-15s [%(levelname)-6s] %(message)s')

    usage = "%%prog [options] MODULE\n\n" \
            "Available modules:\n%s" % \
            "\n".join([ "  %s" % x for x in available_modules() ])

    parser = OptionParser(usage=usage)
    parser.add_option("-v", "--variant", dest="variant", default=None,
                      type="int", help="Variant for analysis module")
    parser.add_option("-t", dest="t_dir", default='./t/',
                      help="Directory of T (translated) texts\n" \
                           "[default: %default]")
    parser.add_option("-o", dest="o_dir", default='./o/',
                      help="Directory of O (original) texts " \
                           "[default: %default]")
    parser.add_option("--auto-outfile", dest="auto_outfile",
                      action="store_true",
                      help="Write output to MODULE[_VARIANT].arff")

    options, args = parser.parse_args()

    try:
        module_name = args[0]
        module = __import__("translationese.%s" % module_name, \
                            fromlist=module_name)
    except IndexError:
        parser.error("No MODULE specified")
    except Exception, ex:
        parser.error(ex)

    for dir_path in options.t_dir, options.o_dir:
        if not os.path.isdir(dir_path):
            parser.error("No such directory %r (run with --help)" % dir_path)

    outfile = get_output_stream(options.auto_outfile, options.variant, \
                                module_name)

    main(module, options.o_dir, options.t_dir, variant=options.variant, \
            stream=outfile)
    if _timer: _timer.finish()
