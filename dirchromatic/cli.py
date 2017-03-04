from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
from argparse import ArgumentParser

from .logger import Logger
from .types import TypeReader, ReadingError
from .util import module

def add_options(parser):
    parser.add_argument('-t', '--types', action='store', dest='types_file', default='types.yaml', help='type file configuration')
    parser.add_argument('-s', '--template', action='store', dest='template', default='template.tmpl', help='dircolors file template')
    parser.add_argument('-o', '--output', action='store', dest='output', default='.dircolors', help='output file name')

def read_types(types_file):
    reader = TypeReader(types_file)
    return reader.get_types()

def main():
    log = Logger()
    try:
        parser = ArgumentParser()
        add_options(parser)
        options = parser.parse_args()
        types = read_types(options.types_file)
    except ReadingError as e:
        log.error('%s' % e)
    except KeyboardInterrupt:
        exit(1)
