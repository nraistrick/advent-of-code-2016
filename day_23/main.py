from common.common import get_file_lines
from day_23.toggled_assembly_runner import ToggledAssemblyRunner


def main():
    lines = [line for line in get_file_lines("input.txt")]
    runner = ToggledAssemblyRunner(lines)
    runner.registry['a'] = 12

    print "Running assembunny instructions..."
    runner.execute()

    print "Final registry values: %s " % str(runner.registry)


if __name__ == '__main__':
    main()
