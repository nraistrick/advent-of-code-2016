"""
Run a series of input 'assembunny' instructions to find the initial
register values to start a monorail
"""


class AssemblyRunner(object):
    """
    Runs a provided collection of 'assembunny' instructions
    """
    COPY = "cpy"
    INCREMENT = "inc"
    DECREMENT = "dec"
    JUMP = "jnz"

    def __init__(self, lines=None):
        """
        :param list[str] lines: The lines of code to execute
        """
        self.lines = lines or []
        self.current_line = 0
        self.registry = self.create_registry()
        self.commands = {self.COPY:      self.copy,
                         self.JUMP:      self.jump,
                         self.INCREMENT: self.increment,
                         self.DECREMENT: self.decrement}

    @staticmethod
    def create_registry():
        """
        :rtype: dict
        """
        return {'a': 0, 'b': 0, 'c': 0, 'd': 0}

    def get_instructions(self):
        """
        Iterates through the provided instructions

        :rtype: collections.Iterable[str]
        """
        self.current_line = 0
        while self.current_line < len(self.lines):
            yield self.lines[self.current_line]
            self.current_line += 1

    def translate(self, value):
        """
        Translates a provided identifier into its equivalent value.
        * No translation is done if an integer is provided.

        :param str value: The value to translate into its equivalent integer
        :rtype: int

        >>> runner = AssemblyRunner([])
        >>> runner.translate('a')
        0
        >>> runner.translate('1')
        1
        >>> runner.translate('-1')
        -1
        """
        unsigned_value = value.lstrip('-')
        return int(value) if unsigned_value.isdigit() else self.registry[value]

    def copy(self, value, register):
        """
        Copies the provided value into the register

        :param str value: Can be a register name or a value
        :type register: str

        >>> runner = AssemblyRunner()
        >>> runner.copy('1', 'a')
        >>> runner.copy('5', 'b')
        >>> sorted(runner.registry.items())
        [('a', 1), ('b', 5), ('c', 0), ('d', 0)]
        """
        self.registry[register] = self.translate(value)

    def jump(self, condition, distance):
        """
        :param str condition: Executes the jump provided the value of this is
        equal to 0; can be a register name or value
        :param str distance: Represents the number of lines to jump by;
        can be a register name or value
        :returns: True if the jump executed and False otherwise
        :rtype: bool

        >>> runner = AssemblyRunner()
        >>> runner.current_line
        0
        >>> return_value = runner.jump('1', '5')
        >>> runner.current_line, return_value
        (4, True)
        >>> return_value = runner.jump('1', '-2')
        >>> runner.current_line, return_value
        (1, True)
        >>> return_value = runner.jump('0', '2')
        >>> runner.current_line, return_value
        (1, False)
        """
        if self.translate(condition) != 0:
            self.current_line += self.translate(distance)

            # Adjust the line so the next instruction we execute
            # is the one we jumped to
            self.current_line -= 1

            return True

        return False

    def increment(self, register):
        """
        :param str register: The register to increase the value of by one

        >>> runner = AssemblyRunner()
        >>> runner.increment('a')
        >>> runner.increment('a')
        >>> runner.increment('c')
        >>> sorted(runner.registry.items())
        [('a', 2), ('b', 0), ('c', 1), ('d', 0)]
        """
        self.registry[register] += 1

    def decrement(self, register):
        """
        :param str register: The register to decrease the value of by one

        >>> runner = AssemblyRunner()
        >>> runner.decrement('b')
        >>> runner.decrement('b')
        >>> runner.decrement('d')
        >>> sorted(runner.registry.items())
        [('a', 0), ('b', -2), ('c', 0), ('d', -1)]
        """
        self.registry[register] -= 1

    def execute_instruction(self, instruction):
        """
        Calls the appropriate method to execute the provided instruction

        :type instruction: str
        """
        command, _, arguments = instruction.partition(' ')
        self.commands[command](*arguments.split(' '))

    def execute(self):
        """
        Runs available instructions to update the internal registry

        We can set, increment and decrement values
        >>> runner = AssemblyRunner(['cpy 1 a'])
        >>> runner.execute()
        >>> runner.registry['a']
        1
        >>> runner = AssemblyRunner(['inc b'])
        >>> runner.execute()
        >>> runner.registry['b']
        1
        >>> runner = AssemblyRunner(['dec c'])
        >>> runner.execute()
        >>> runner.registry['c']
        -1

        We can jump forward past other lines
        >>> runner = AssemblyRunner(['jnz 1 2', 'inc a'])
        >>> runner.execute()
        >>> runner.registry['a']
        0

        Jumps will only run if their first argument is non-zero
        >>> runner = AssemblyRunner(['jnz 0 2', 'inc a'])
        >>> runner.execute()
        >>> runner.registry['a']
        1

        We can jump backwards and repeat previous lines
        >>> runner = AssemblyRunner(['cpy 2 a', 'dec a', 'inc b', 'jnz a -2'])
        >>> runner.execute()
        >>> sorted(runner.registry.items()) #doctest: +ELLIPSIS
        [('a', 0), ('b', 2)...]

        We throw an exception on invalid commands
        >>> runner = AssemblyRunner(["invalid 2 a"])
        >>> runner.execute() # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        KeyError: 'invalid'
        """
        for i in self.get_instructions():
            self.execute_instruction(i)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
