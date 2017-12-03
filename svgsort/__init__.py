#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""svgsort

Usage:
  svgsort <in> <out> [--reverse]
  svgsort -h

Options:
  --reverse   Attempt to reverse path directions (Warning, this is
  experimental)

Examples:
  svgsort input.svg out.svg
  svgsort input.svg out.svg --reverse
"""


__ALL__ = ['Svgsort']

import sys
import traceback

from svgsort.svgsort import Svgsort


VERBOSE = True



def run():

  from docopt import docopt
  args = docopt(__doc__, version='svgsort 0.0.1')
  main(args)


def main(args):

  try:
    _in = args['<in>']
    out = args['<out>']
    reverse = args['--reverse']
    if VERBOSE:
      print('reverse: {:b}'.format(reverse))

    Svgsort().load(_in, verbose=VERBOSE)\
             .sort(reverse, verbose=VERBOSE)\
             .save(out)
    print('wrote: ', out)
  except Exception:
    traceback.print_exc(file=sys.stdout)
    exit(1)



if __name__ == '__main__':
  run()

