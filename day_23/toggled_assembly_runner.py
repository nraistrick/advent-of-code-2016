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
