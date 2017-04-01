"""
Shared functionality for advent of code
"""
from itertools import izip_longest


def get_file_lines(file_path):
    """
    :type file_path: str
    :return:
    """
    with open(file_path, "r") as instructions:
        for line in instructions:
            yield line.strip('\n')


def grouper(iterable, chunk_size, fill_value=None):
    """
    Chunks an iterable into a series of tuples

    :type iterable: collections.Iterable
    :type chunk_size: int
    :param fill_value: The default object to insert to pad an empty group
    :rtype: list[tuple]
    """
    args = [iter(iterable)] * chunk_size
    return izip_longest(*args, fillvalue=fill_value)
