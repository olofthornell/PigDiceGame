"""Holds the personality of the cpu player."""


class Intelligence():
    """Cpu personality."""

    def __init__(self):
        """Init the object."""
        self.coward = 4
        self.moderate = 15
        self.bold = 25

    def get_coward(self):
        """Set cpu player to a coward."""
        return self.coward

    def get_moderate(self):
        """Set cpu player to moderate."""
        return self.moderate

    def get_bold(self):
        """Set cpu player to bold."""
        return self.bold
