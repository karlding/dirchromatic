import sys

from .colour import Colour
from .level import Level

class Logger():
    def __init__(self, level = Level.INFO):
        self.set_level(level)

    def set_level(self, level):
        self._level = level

    def log(self, level, message):
        if (level >= self._level):
            print('%s%s%s' % (self._color(level), message, self._reset()))

    def debug(self, message):
        self.log(Level.DEBUG, message)

    def info(self, message):
        self.log(Level.INFO, message)

    def error(self, message):
        self.log(Level.ERROR, message)

    def _color(self, level):
        """
        Get a color (terminal escape sequence) according to a level.
        """
        if not sys.stdout.isatty():
            return ''
        elif level < Level.DEBUG:
            return ''
        elif Level.DEBUG <= level < Level.INFO:
            return Colour.YELLOW
        elif Level.INFO <= level < Level.ERROR:
            return Colour.GREEN
        elif Level.ERROR <= level:
            return Colour.RED

    def _reset(self):
        '''
        Get a reset color (terminal escape sequence).
        '''
        if not sys.stdout.isatty():
            return ''
        else:
            return Colour.RESET
