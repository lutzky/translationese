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

class Timer:
    def __init__(self, report_every = 10, stream=sys.stderr):
        self.report_every = report_every
        self.stream = stream

    def start(self):
        self.started_at = time.time()
        self.count = 0

    def increment(self):
        self.count += 1
        if self.count % self.report_every == 0:
            elapsed = time.time() - self.started_at
            average_ms = 1000.0 * (elapsed / self.count)
            self.stream.write(\
                    "\r[%5d] %d seconds elapsed, (%.2f ms each)" \
                    % (self.count, elapsed, average_ms))

    def finish(self):
        self.stream.write("\n")

_timer = None

def analyze_file(f, analyzer_module, variant=None):
    analysis = translationese.Analysis(f)

    if variant is not None:
        return analyzer_module.quantify_variant(analysis, variant)
    else:
        return analyzer_module.quantify(analysis)

def analyze_directory(dir_to_analyze, expected_class, analyzer_module, stream,
                      variant=None):
    if variant is None:
        attributes = analyzer_module.attributes
    else:
        attributes = analyzer_module.variant_attributes[variant]

    for filename in sorted(os.listdir(dir_to_analyze)):
        with open(os.path.join(dir_to_analyze, filename)) as f:
            try:
                result = analyze_file(f, analyzer_module, variant)
            except:
                print >> sys.stderr, "Error analyzing file %s" % filename
                raise

            line = ",".join([str(result[x]) for x in attributes])

            print >> stream, "%s,%s" % (line, expected_class)
            if _timer: _timer.increment()

def main(analyzer_module, o_dir, t_dir, stream=sys.stdout, variant=None):
    if variant is None:
        if hasattr(analyzer_module, "attributes"):
            attributes = analyzer_module.attributes
        else:
            raise translationese.MissingVariant("%s requires a variant to be specified" % \
                                                analyzer_module.__name__)
    else:
        try:
            attributes = analyzer_module.variant_attributes[variant]
        except AttributeError, ex:
            raise translationese.NoVariants("%s does not support variants" % \
                                            analyzer_module.__name__)
        except IndexError, ex:
            raise translationese.NoSuchVariant(analyzer_module)

    print >> stream, "@relation translationese"

    for attribute in attributes:
        print >> stream, "@attribute %s numeric" % repr(attribute)

    # Class attribute should be last, as this is the weka default.
    print >> stream, "@attribute class { T, O }"
    print >> stream
    print >> stream, "@data"

    if _timer: _timer.start()

    analyze_directory(o_dir, "O", analyzer_module, stream, variant)
    analyze_directory(t_dir, "T", analyzer_module, stream, variant)

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

if __name__ == '__main__':
    from optparse import OptionParser
    _timer = Timer()

    usage="%%prog [options] MODULE\n\n" \
            "Available modules:\n%s" % \
            "\n".join([ "  %s" % x for x in available_modules() ])

    parser = OptionParser(usage=usage)
    parser.add_option("-v", "--variant", dest="variant", default=None,
                      type="int", help="Variant for analysis module")
    parser.add_option("-t", dest="t_dir", default='./o/',
                      help="Directory of T (translated) texts\n[default: %default]")
    parser.add_option("-o", dest="o_dir", default='./t/',
                      help="Directory of O (original) texts [default: %default]")
    parser.add_option("--auto-outfile", dest="auto_outfile", action="store_true",
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
