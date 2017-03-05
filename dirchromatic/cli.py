from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys
from argparse import ArgumentParser

from .logger import Logger
from .generator import Generator, DispatchError
from .types import TypeReader, ReadingError
from .writer import OutputWriter
from .util import module

def add_options(parser):
    parser.add_argument('-t', '--types', action='store', dest='types_file', default='types.yaml', help='type file configuration')
    parser.add_argument('-s', '--template', action='store', dest='template', default='template.tmpl', help='dircolors file template')
    parser.add_argument('-o', '--output', action='store', dest='output', default='.dircolors', help='output file name')

def read_types(types_file):
    reader = TypeReader(types_file)
    return reader.get_types()

def write_file(template, output_file, data):
    writer = OutputWriter(template, output_file)
    writer.write(data)

def main():
    log = Logger()
    try:
        parser = ArgumentParser()
        add_options(parser)
        options = parser.parse_args()
        types = read_types(options.types_file)
        if not isinstance(types, list):
            raise ReadingError('Types file must be a list of types')
        generator = Generator(os.path.dirname(options.types_file))
        line_buffer = generator.generate(types)
        template = open(options.template, 'r')
        fd = open(options.output, 'w')
        write_file(template, fd, line_buffer)
    except ReadingError as e:
        log.error('%s' % e)
    except KeyboardInterrupt:
        exit(1)
