from day_12.assembly_runner import AssemblyRunner


class OutputAssemblyRunner(AssemblyRunner):
    OUT = "out"

    def __init__(self, lines=None):
        super(OutputAssemblyRunner, self).__init__(lines)
        self.output_data = ""
        self.commands[self.OUT] = self.output

    def output(self, value):
        """
        :type value: str
        """
        self.output_data += str(self.translate(value))

    def execute(self):
        """
        Runs available instructions to update the internal registry
        """
        for i in self.get_instructions():
            self.execute_instruction(i)

            if len(self.output_data) == 8:
                break

        return self.output_data

