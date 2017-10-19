"""
Finds the first second when the slots in a series of spinning discs are
aligned so a capsule will fall through them when it is dropped.
"""

import itertools
from day_15.disc import Disc


def move_discs_forward(discs):
    """
    :type discs: list[Disc]
    :rtype: None
    """
    for d in discs:
        d.tick_forward()


def all_discs_aligned(discs):
    """
    Check if the capsule will successfully fall through the current
    disc setup. There is a second delay for the capsule to reach the next
    disc in the provided sequence.

    :type discs: list[Disc]
    :rtype: bool
    """
    for i, disc in enumerate(discs):
        seconds_until_capsule_arrives = i + 1
        if not disc.slot_aligned_in(seconds_until_capsule_arrives):
            return False

    return True


def main():
    discs = [Disc(11, 13),
             Disc(0, 5),
             Disc(11, 17),
             Disc(0, 3),
             Disc(2, 7),
             Disc(17, 19),
             Disc(0, 11)]

    for second in itertools.count():
        if all_discs_aligned(discs):
            print "The first time you can drop the capsule is at %d seconds" % second
            break
        move_discs_forward(discs)


if __name__ == '__main__':
    main()
