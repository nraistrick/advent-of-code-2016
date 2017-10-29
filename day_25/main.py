from common.common import get_file_lines
from day_25.output_assembly_runner import OutputAssemblyRunner


def main():
    lines = [line for line in get_file_lines("input.txt")]
    for i in xrange(1, 1000):
        runner = OutputAssemblyRunner(lines)
        runner.registry['a'] = i

        generated_characters = runner.execute()
        print "Initialised at %3d : %s" % (i, generated_characters)
        if "01010101" in generated_characters:
            print "Lowest positive integer: %d" % i
            break


if __name__ == '__main__':
    main()
