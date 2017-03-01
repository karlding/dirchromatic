from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
from argparse import ArgumentParser

from .util import module

def add_options(parser):
    parser.add_argument('-types', action='append', dest='types', default='types.yaml', help='type file configuration')
    parser.add_argument('-template', action='append', dest='template', default='template.tmpl', help='dircolors file template')
    parser.add_argument('-output', action='append', dest='output', default='.dircolors', help='output file name')

def main():
    try:
        parser = ArgumentParser()
        add_options(parser)
        options = parser.parse_args()
    except KeyboardInterrupt:
        exit(1)
