"""
For a given salt value, calculate a set of keys for a one-time encryption pad by:

* Finding the MD5 sum of a salt and an increasing integer value (starting at 0)
* Looking for a triple repeating digit in each sum e.g. '777'
* If a triple repeating digit is found, check if that same digit is repeated at
    least 5 times in one of the next 1000 hashes i.e. '77777'
* If it is, that sum is one of your one-time pad keys

We want to know what is the 64th sum to form your one-time pad
"""

from day_14.one_time_pad_finder import get_one_time_pad_values


def main():
    values = get_one_time_pad_values("cuanljph", 64)
    print "64th one-time pad key: %s" % str(values[63])


if __name__ == "__main__":
    main()
