"""Holds the personality of the cpu player."""


class Intelligence:
    """Cpu personality."""

    def __init__(self):
        """Init the object."""
        self._coward = 4
        self._moderate = 15
        self._bold = 25

    def coward(self):
        """Set cpu player to a coward."""
        return self._coward

    def moderate(self):
        """Set cpu player to moderate."""
        return self._moderate

    def bold(self):
        """Set cpu player to bold."""
        return self._bold
