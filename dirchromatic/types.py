import os.path

import yaml

from .util import string

class TypeReader(object):
    def __init__(self, types_file_path):
        self._types = self._read(types_file_path)

    def _read(self, types_file_path):
        try:
            _, ext = os.path.splitext(types_file_path)
            with open(types_file_path) as fin:
                data = yaml.safe_load(fin)
            return data
        except Exception as e:
            msg = string.format_lines(str(e))
            raise ReadingError('Could not read types file:\n%s' % msg)

    def get_types(self):
        return self._types

class ReadingError(Exception):
    pass
