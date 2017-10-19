class Disc(object):
    """
    Models a disc containing a single slot which a capsule can fall through
    """
    SLOT_POSITION = 0

    def __init__(self, current_position, positions):
        """
        :type: int
        :type positions: int

        >>> Disc(1, 0) # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: Must have more than one position

        >>> Disc(2, 2) # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: Current position must be within the allowed range...

        """
        if positions <= 1:
            raise ValueError("Must have more than one position")

        self.positions = positions
        if current_position > self.max_position:
            raise ValueError("Current position must be within the allowed "
                             "range of positions")

        self._current_position = current_position

    @property
    def current_position(self):
        return self._current_position

    @property
    def max_position(self):
        return self.positions - 1

    def tick_forward(self, ticks=1):
        """
        >>> d = Disc(0, 2)
        >>> d.current_position == 0
        True
        >>> d.tick_forward()
        >>> d.current_position == 1
        True
        >>> d.tick_forward()
        >>> d.current_position == 0
        True
        """
        self._current_position = (self.current_position + ticks) % self.positions

    @property
    def slot_aligned(self):
        """
        >>> d = Disc(0, 2)
        >>> d.slot_aligned
        True
        >>> d.tick_forward()
        >>> d.slot_aligned
        False
        >>> d.tick_forward()
        >>> d.slot_aligned
        True
        """
        if self.current_position == self.SLOT_POSITION:
            return True
        return False

    def slot_aligned_in(self, ticks):
        """
        :type ticks: int
        :rtype: bool

        >>> d = Disc(0, 2)
        >>> d.slot_aligned_in(0) # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: ...
        >>> d.slot_aligned_in(1)
        False
        >>> d.slot_aligned_in(2)
        True
        >>> d.slot_aligned_in(3)
        False
        >>> d.slot_aligned_in(4)
        True
        >>> d.current_position
        0
        """
        if ticks == 0:
            raise ValueError("Must be looking forward by at least one tick")

        current_position = self.current_position
        self.tick_forward(ticks)
        aligned = self.slot_aligned
        self._current_position = current_position

        return aligned
