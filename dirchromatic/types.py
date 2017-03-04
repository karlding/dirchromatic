import os.path

import yaml

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
            msg = str(e)
            raise ReadingError('Could not read types file:\n%s' % msg)

    def _get_types(self):
        return self._types

class ReadingError(Exception):
    pass
