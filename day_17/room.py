from common.common import get_md5_hash


class Room(object):
    DOOR_OPEN_CHARACTERS = ('b', 'c', 'd', 'e', 'f')

    def __init__(self, passcode, previous_steps=None):
        """
        :type passcode: str
        :param str previous_steps: Abbreviations of the previous directions
        moved e.g. "DRUL"

        >>> r = Room("hijkl")
        >>> r.can_go_up, r.can_go_down, r.can_go_left, r.can_go_right
        (True, True, True, False)
        """
        self.passcode = passcode
        self.previous_steps = previous_steps
        self.hash = self.get_hash()

    def get_hash(self):
        """
        :rtype: str

        >>> Room("hijkl").get_hash()
        'ced9'
        >>> Room("hijkl", "D").get_hash()
        'f2bc'
        >>> Room("hijkl", "DR").get_hash()
        '5745'
        """
        value = self.passcode
        if self.previous_steps:
            value += self.previous_steps

        return get_md5_hash(value)[:4]

    @property
    def can_go_up(self):
        return self.hash[0] in self.DOOR_OPEN_CHARACTERS

    @property
    def can_go_down(self):
        return self.hash[1] in self.DOOR_OPEN_CHARACTERS

    @property
    def can_go_left(self):
        return self.hash[2] in self.DOOR_OPEN_CHARACTERS

    @property
    def can_go_right(self):
        return self.hash[3] in self.DOOR_OPEN_CHARACTERS


if __name__ == '__main__':
    import doctest
    doctest.testmod()
