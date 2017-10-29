from copy import deepcopy
from day_12.assembly_runner import AssemblyRunner


class ToggledAssemblyRunner(AssemblyRunner):
    """
    Runs a provided collection of 'assembunny' instructions
    """
    TOGGLE = "tgl"

    def __init__(self, lines=None):
        """
        :param list[str] lines: The lines of code to execute
        """
        super(ToggledAssemblyRunner, self).__init__(lines)
        self.commands[self.TOGGLE] = self.toggle

        # Holds snapshots of the registry at previous lines
        self.old_register_store = {}

    @staticmethod
    def toggle_instruction(instruction):
        """
        :type instruction: str
        :rtype: str

        Toggles an instruction to a different type of instruction e.g.

        >>> ToggledAssemblyRunner.toggle_instruction("inc a")
        'dec a'
        >>> ToggledAssemblyRunner.toggle_instruction("dec b")
        'inc b'
        >>> ToggledAssemblyRunner.toggle_instruction("jnz a 1")
        'cpy a 1'
        >>> ToggledAssemblyRunner.toggle_instruction("cpy a b")
        'jnz a b'
        """
        mapper = {ToggledAssemblyRunner.INCREMENT: ToggledAssemblyRunner.DECREMENT,
                  ToggledAssemblyRunner.DECREMENT: ToggledAssemblyRunner.INCREMENT,
                  ToggledAssemblyRunner.COPY:      ToggledAssemblyRunner.JUMP,
                  ToggledAssemblyRunner.JUMP:      ToggledAssemblyRunner.COPY,
                  ToggledAssemblyRunner.TOGGLE:    ToggledAssemblyRunner.INCREMENT}

        instruction = instruction.split(" ")
        instruction[0] = mapper[instruction[0]]
        return " ".join(instruction)

    def toggle(self, value):
        """
        :param str value: Indicates which line to perform a toggle on
        relative to the current line; can be a register name or value

        >>> runner = ToggledAssemblyRunner(['tgl 1',
        ...                                 'inc a'])
        >>> runner.execute()
        >>> runner.registry['a']
        -1

        >>> runner = ToggledAssemblyRunner(['cpy 2 a',
        ...                                 'tgl a',
        ...                                 'tgl a',
        ...                                 'tgl a',
        ...                                 'cpy 1 a',
        ...                                 'dec a',
        ...                                 'dec a'])
        >>> runner.execute()
        >>> runner.registry['a']
        3
        """
        offset = self.translate(value)
        toggled_line = self.current_line + offset
        if toggled_line < len(self.lines):
            self.lines[toggled_line] = self.toggle_instruction(self.lines[toggled_line])

    def multiply_difference(self, multiple, line_jump):
        """
        Multiplies the difference between values in current registry values and
        values in a registry at a previous line. This improves the efficiency with
        which we can carry out repeating loops in 'assembunny' calculations.

        :param int multiple: The multiplication factor
        :param int line_jump: A relative number of lines to move
        """
        updated_line = self.current_line + line_jump

        # Check we're looking at a valid line
        if updated_line < 0 or updated_line >= len(self.lines):
            return

        # Multiply the differences in value with the old registry
        old_registry = self.old_register_store[updated_line]
        for key in self.registry:
            difference = self.registry[key] - old_registry[key]
            self.registry[key] += difference * multiple

    def jump(self, condition, distance):
        if self.translate(condition) == 0:
            return

        line_jump = self.translate(distance)
        if line_jump > 0 or condition.isdigit():
            super(ToggledAssemblyRunner, self).jump(condition, distance)

        # We're jumping backwards so let's increase the efficiency of
        # instruction execution by using multiplication
        self.multiply_difference(self.translate(condition), line_jump)

    def execute(self):
        """
        Runs available instructions to update the internal registry
        """
        for i in self.get_instructions():
            self.old_register_store[self.current_line] = deepcopy(self.registry)
            self.execute_instruction(i)
