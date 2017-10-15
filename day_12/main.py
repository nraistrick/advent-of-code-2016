from common.common import get_file_lines
from day_12.assembly_runner import AssemblyRunner


def main():
    lines = [line for line in get_file_lines("input.txt")]
    runner = AssemblyRunner(lines)

    print "Running assembunny instructions..."
    runner.execute()

    print "Final registry values: %s " % str(runner.registry)


if __name__ == '__main__':
    main()
