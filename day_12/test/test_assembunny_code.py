import os
from unittest import TestCase

from common.common import get_file_lines
from day_12.assembly_runner import AssemblyRunner


class TestAssembunnyCode(TestCase):
    def test_create_registers(self):
        directory = os.path.dirname(os.path.abspath(__file__))
        lines = [line for line in get_file_lines("%s/%s" % (directory, "test_input.txt"))]
        runner = AssemblyRunner(lines)
        runner.execute()
        self.assertEqual(runner.registry, {'a': 42, 'b': 0, 'c': 0, 'd': 0})
