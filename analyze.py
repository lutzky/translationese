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
import errno

class Timer:
    """Simple progress reporter. Call ``increment`` for every event
    which occurs, and every ``report_every`` seconds the count and
    average time will be displayed."""

    def __init__(self, report_every=1, stream=sys.stderr):
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

    def output(self):
        elapsed = time.time() - self.started_at
        average_ms = 1000.0 * (elapsed / self.count)
        if self.stream:
            self.stream.write(\
                    "\r[%5d] %d seconds elapsed, (%.2f ms each)" \
                    % (self.count, elapsed, average_ms))
            self.stream.flush()

    def increment(self):
        """Report an event as having occured."""
        self.count += 1
        if time.time() - self.prevtime > self.report_every:
            self.output()
            self.prevtime = time.time()

    def stop(self):
        """Stop the timer, properly formatting end-of-line."""
        self.output()
        if self.stream:
            self.stream.write("\n")

def analyze_file(filename, analyzer_module, variant=None):
    with translationese.Analysis(filename=filename) as analysis:
        if variant is not None:
            return analyzer_module.quantify_variant(analysis, variant)
        else:
            return analyzer_module.quantify(analysis)

def analyze_directory(dir_to_analyze, expected_class, analyzer_module,
                      variant, timer):
    results = []

    for filename in sorted(os.listdir(dir_to_analyze)):
        if filename.endswith(".analysis"):
            # This is a cached analysis, skip it.
            continue
        filename = os.path.join(dir_to_analyze, filename)
        try:
            result = analyze_file(filename, analyzer_module, variant)
            timer.increment()
        except:
            logging.error("Error analyzing file %s", filename)
            raise

        results.append((result, expected_class))

    return results

def print_results(results, stream, timer):
    attributes = set()

    print >> stream, "@relation translationese"

    logging.info("Merging result keys")
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

    logging.info("Printing results")

    timer.start()
    for result, expected_class in results:
        stream.write('{')

        sparse_attributes = ['%d %s' % (i, result[attribute])
                             for i, attribute in enumerate(attributes)
                             if result.get(attribute, 0)]

        sparse_attributes.append('%d %s' % (len(attributes), expected_class))
        stream.write(', '.join(sparse_attributes))
        print >> stream, '}'
        timer.increment()
    timer.stop()

def main(analyzer_module, o_dir, t_dir, stream=sys.stdout, variant=None,
         timer_stream=sys.stdout):
    """Internal, testable main() function for analysis."""
    if variant is None:
        if not hasattr(analyzer_module, "quantify"):
            raise MissingVariant("%s requires a variant to be specified" % \
                                 analyzer_module.__name__)
    elif not hasattr(analyzer_module, "quantify_variant"):
        raise translationese.NoVariants("%s does not support variants" % \
                                        analyzer_module.__name__)

    timer = Timer(stream=timer_stream)

    results = []

    logging.info("Analyzing 'O' directory %s", o_dir)
    timer.start()
    results += analyze_directory(o_dir, "O", analyzer_module, variant, timer)
    timer.stop()

    logging.info("Analyzing 'T' directory %s", t_dir)
    timer.start()
    results += analyze_directory(t_dir, "T", analyzer_module, variant, timer)
    timer.stop()

    print_results(results, stream, timer)

def import_translationese_module(module_name):
    if ':' in module_name:
        module_name = module_name.split(':')[0]
    return __import__('translationese.%s' % module_name,
                      fromlist='translationese')

def module_proper_name(module_name):
    """If ``module_name`` is an ordinarily quantifiable module, returns it
    as-is. If it requires a variant, ``module_name*`` is returned. If it is
    not quantifiable, ``None`` is returned."""

    module = import_translationese_module(module_name)

    if hasattr(module, 'quantify'):
        return module_name
    elif hasattr(module, 'quantify_variant'):
        variants = [ '%s:%d' % (module_name, v) for v in module.VARIANTS ]
        return ' '.join(variants)
    else:
        return None

def formatted_available_modules():
    iterator = pkgutil.iter_modules(['translationese'])
    result = (module_proper_name(x[1]) for x in iterator)
    return ' '.join(filter(None, result))

def available_modules_imported():
    iterator = pkgutil.iter_modules(['translationese'])
    for _, module_name, _ in iterator:
        module = import_translationese_module(module_name)
        if hasattr(module, 'quantify') or hasattr(module, 'quantify_variant'):
            yield module

def get_output_stream(outfile, module_name, dest_dir=None):
    if dest_dir:
        try:
            os.makedirs(dest_dir)
        except OSError, ex:
            if ex.errno == errno.EEXIST:
                pass
            else:
                raise
    else:
        dest_dir = '.'

    if not outfile:
        outfile = "%s.arff" % module_name

    outstream = open(os.path.join(dest_dir, outfile), "w")

    return outstream

def analyze_all_modules(o_dir, t_dir, dest_dir):
    for module in available_modules_imported():
        module_name = module.__name__.split('.')[-1]
        logging.info("Analyzing with %s", module_name)
        if hasattr(module, 'VARIANTS'):
            for v in module.VARIANTS:
                logging.info("Variant %d", v)
                outfile = get_output_stream(None, '%s:%d' % (module_name, v),
                                            dest_dir)
                cmdline_main_one_module(module, o_dir, t_dir, v, outfile)
        else:
            outfile = get_output_stream(None, module_name, dest_dir)
            cmdline_main_one_module(module, o_dir, t_dir, None, outfile)

def cmdline_main():
    """External main() function for calling from commandline."""
    from argparse import ArgumentParser

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)-15s [%(levelname)-6s] %(message)s')

    description = '''
    Run a translationese analysis of T_DIR and O_DIR, using MODULE. Output
    is in weka-compatible ARFF format.

    Specify 'ALL' as the module to automatically run all possible variants on
    all possible modules.
    '''

    epilog = '''
    Modules marked with a colon (:) indicate variants of the same module.
    OUTFILE is MODULE_NAME.arff (including variant, if present).
    '''

    parser = ArgumentParser(description=description, epilog=epilog)
    parser.add_argument('module_names', type=str, metavar='MODULE',
                        nargs='+',
                        help='Available modules: %s (or ALL)' \
                        % formatted_available_modules())
    parser.add_argument("-t", dest="t_dir", default='./t/',
                        help="Directory of T (translated) texts " \
                             "[default: %(default)s]")
    parser.add_argument("-o", dest="o_dir", default='./o/',
                        help="Directory of O (original) texts " \
                             "[default: %(default)s]")
    parser.add_argument("--outfile", dest="outfile",
                        help="Write output to OUTFILE.")
    parser.add_argument("-d", "--dest-dir", dest="dest_dir",
                        help="OUTFILE[s] will be created in DEST_DIR.")

    args = parser.parse_args()

    for dir_path in args.t_dir, args.o_dir:
        if not os.path.isdir(dir_path):
            parser.error("No such directory %r (run with --help)" % dir_path)

    if args.module_names[0] == 'ALL':
        analyze_all_modules(args.o_dir, args.t_dir, args.dest_dir)
    else:
        for module_name in args.module_names:
            outfile = get_output_stream(args.outfile, module_name,
                                        args.dest_dir)
            module = import_translationese_module(module_name)
            if ":" in module_name:
                variant = int(module_name.split(":")[1])
            else:
                variant = None
            cmdline_main_one_module(module, args.o_dir, args.t_dir,
                                    variant, outfile)

def cmdline_main_one_module(module, o_dir, t_dir, variant, outfile):
    logging.info("Output will be written to %s", outfile.name)
    main(module, o_dir=o_dir, t_dir=t_dir,
         variant=variant, stream=outfile)

if __name__ == '__main__':
    cmdline_main()
