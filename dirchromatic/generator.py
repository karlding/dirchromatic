import os

import yaml

from .logger import Logger

class Generator(object):
    def __init__(self, base_directory):
        self._log = Logger()
        self._setup_context(base_directory)

    def _setup_context(self, base_directory):
        path = os.path.abspath(os.path.realpath(
            os.path.expanduser(base_directory)))
        if not os.path.exists(path):
            raise DispatchError('Nonexistent base directory')
        self._path = path

    def generate(self, types):
        log = self._log
        for type in types:
            try:
                self._log.info('Generating types for %s' % type['src'])
                self._generate(type)
            except Exception as e:
                self._log.error('Error processing %s' % type)

    def _generate(self, type):
        path = os.path.join(self._path, type['src'])
        try:
            with open(path) as fin:
                data = yaml.safe_load(fin)
            if data:
                longest = max(map(len, data))
                for ext in data:
                    print(('%s' % ext).ljust(longest + 2) + '%s' % type['colour'])# + '%s' % (ext, type['colour']))
        except Exception as e:
            print(e)

class DispatchError(Exception):
    pass
