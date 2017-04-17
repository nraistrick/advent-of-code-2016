"""
Organise a series of bots to pass and compare a collections of microchips
"""

import re

from common.common import get_file_lines
from containers.bot import Bot
from containers.output import Output

BOT_IDENTIFIER = "bot"
MICROCHIP_IDENTIFIER = "value"
OUTPUT_IDENTIFIER = "output"


def get_bot_ids(text):
    """
    :param list[str] text: The provided bot instructions
    :rtype: list[int]
    """
    return get_container_object_ids(text, BOT_IDENTIFIER)


def get_output_ids(text):
    """
    :param list[str] text: The provided bot instructions
    :rtype: list[int]
    """
    return get_container_object_ids(text, OUTPUT_IDENTIFIER)


def get_container_object_ids(text, container_id):
    """
    Gets a list of bot or output IDs

    :param list[str] text: The provided bot instructions
    :type container_id: str
    :rtype: list[int]
    """
    if container_id != BOT_IDENTIFIER and container_id != OUTPUT_IDENTIFIER:
        raise ValueError("Please specify a valid item to get IDs for")

    ids = []
    search_string = "(bot) (?P<%s>[0-9]+)" % container_id
    for line in text:
        for match in re.finditer(search_string, line):
            item_id = int(match.group(container_id))
            ids.append(item_id)

    return ids


def initialise_containers(text, bots, outputs):
    """
    Parse the provided instructions to put microchips in the correct containers
    and configure links between between bots and outputs

    :param list[str] text: The provided bot instructions
    :type bots: dict[int, Bot]
    :type outputs: dict[int, Output]
    """
    containers = {BOT_IDENTIFIER: bots, OUTPUT_IDENTIFIER: outputs}

    for line in text:
        inputs = line.split(" ")

        if inputs[0] == BOT_IDENTIFIER:
            bot_id = int(inputs[1])
            low_container = inputs[5]
            low_id = int(inputs[6])
            high_container = inputs[-2]
            high_id = int(inputs[-1])

            # Link bots to pass microchips to other bots and outputs
            bots[bot_id].low_chip_destination = containers[low_container][low_id]
            bots[bot_id].high_chip_destination = containers[high_container][high_id]

        elif inputs[0] == MICROCHIP_IDENTIFIER:
            microchip_id = int(inputs[1])
            bot_id = int(inputs[-1])

            # Give microchip to the specified bot
            bots[bot_id].append(microchip_id)

        else:
            raise ValueError("Got unexpected first word for input instruction: %s" % line[0])


def find_bot_to_compare_chips(bots, first_microchip_id, second_microchip_id):
    """
    Find a bot responsible for making a decision between two microchip IDs

    :type bots: dict[int, Bot]
    :type first_microchip_id: int
    :type second_microchip_id: int
    :return: The bot ID
    :rtype: int
    """
    while True:
        for bot_id, bot in bots.iteritems():
            if first_microchip_id in bot and second_microchip_id in bot:
                return bot_id
            if len(bot) == Bot.MAX_MICROCHIPS:
                bot.move_microchips()


def get_microchip_product(bots, outputs):
    """
    Finds the product of the microchip values in the first three outputs 0, 1 and 2.

    :type bots: dict[int, Bot]
    :param outputs: dict[int, Output]
    :return: The product of the first three chip values
    :rtype: int
    """
    while True:
        for bot in bots.values():
            if outputs[0] and outputs[1] and outputs[2]:
                return outputs[0][0] * outputs[1][0] * outputs[2][0]
            if len(bot) == Bot.MAX_MICROCHIPS:
                bot.move_microchips()


def get_initialised_containers(instructions):
    """
    Creates a set of bots and outputs and initialises them according to the
    provided instructions

    :type instructions: list[str]
    :rtype: (dict[int, Bot], dict[int, Output])
    """
    bots = {i: Bot() for i in get_bot_ids(instructions)}
    outputs = {i: Output() for i in get_output_ids(instructions)}
    initialise_containers(instructions, bots, outputs)

    return bots, outputs


def main():
    input_data = [line for line in get_file_lines("input/input.txt")]
    bots, outputs = get_initialised_containers(input_data)

    print "The bot responsible for 17 and 61 is: %d" \
          % find_bot_to_compare_chips(bots, 17, 61)
    print "The product of the first three microchips is: %d" \
          % get_microchip_product(bots, outputs)


if __name__ == '__main__':
    main()
