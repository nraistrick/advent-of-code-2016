import unittest
from containers.output import Output, MicrochipLimitExceeded
from containers.bot import Bot


class TestContainers(unittest.TestCase):
    def test_output_limits_microchips(self):
        output = Output()
        output += [1, 2]
        with self.assertRaises(MicrochipLimitExceeded):
            output.append(3)
        with self.assertRaises(MicrochipLimitExceeded):
            output += [3, 4]

    def test_bot_moves_max_microchips(self):
        bot = Bot()
        bot.low_chip_destination, bot.high_chip_destination = [], []
        with self.assertRaises(ValueError):
            bot.move_microchips()

        bot += ([1, 2])
        bot.move_microchips()


if __name__ == '__main__':
    unittest.main()
