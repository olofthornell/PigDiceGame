"""Holds the personality of the cpu player"""


class Intelligence:
    """Cpu personality"""

    def __init__(self):
        self._coward = 4
        self._moderate = 15
        self._bold = 25

    def coward(self):
        """A cpu player that is a coward"""
        return self._coward

    def moderate(self):
        """A cpu player that is moderate"""
        return self._moderate

    def bold(self):
        """A cpu player that is bold"""
        return self._bold
