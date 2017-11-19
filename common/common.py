"""
Shared functionality for advent of code
"""


def get_file_lines(file_path):
    """
    :type file_path: str
    :return:
    """
    with open(file_path, "r") as instructions:
        for line in instructions:
            yield line.strip('\n')
