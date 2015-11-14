import sys
from file_helper import FileHelper
from instructions import *
from util import *


def create_parse_tree_from_file(filename):
    # Open program file
    parse_tree = []
    file_helper = FileHelper(filename)
    file_helper.open_program_file()

    line = file_helper.read_line()
    while file_helper.has_lines_left():
        line = line.replace(',', '')
        instruction = line[:-1].split()

        # Skip empty lines
        if file_helper.is_empty_line():
            line = file_helper.read_line()
            continue

        # Append parse tree and read new line
        parse_tree.append(instruction)
        line = file_helper.read_line()

    file_helper.close_program_file()
    return parse_tree


def add_opcode_to_parse_tree(parse_tree):
    new_parse_tree = []
    for instruction in parse_tree:
        opcode = Instructions.get_opcode(instruction[0])
        instruction[0] = opcode

        new_parse_tree.append(instruction)

    return new_parse_tree


def convert_decimal_to_binary(decimal_number):

    if is_hex_number(decimal_number):
        integer = int(decimal_number, 16)
    else:
        integer = int(decimal_number)

    binary = bin(integer)
    string = str(binary)
    return string[2:]


def convert_immediate_decimal_to_binary(parse_tree):
    new_parse_tree = []

    for instruction in parse_tree:
        new_instruction = []

        for word in instruction:
            if is_immediate_value(word):
                binary = convert_decimal_to_binary(word[1:])
                new_instruction.append(binary)
                continue

            new_instruction.append(word)

        new_parse_tree.append(new_instruction)

    return new_parse_tree


def convert_register_to_binary(parse_tree):
    new_parse_tree = []

    for instruction in parse_tree:
        new_instruction = []

        for word in instruction:
            if is_register(word):
                register = convert_decimal_to_binary(word[1:])
                new_instruction.append(register)
                continue

            new_instruction.append(word)
        new_parse_tree.append(new_instruction)

    return new_parse_tree


def add_missing_zeros(parse_tree, partition_tree):
    new_parse_tree = []

    for i, instruction in enumerate(parse_tree):
        new_instruction = []
        word_partition = partition_tree[i]

        for partition in word_partition:
            index = partition[0]
            total_bits = partition[1]

            # if index >= len(instruction) the last digits are don't care
            if index >= len(instruction):
                instruction_part = '0'
            else:
                instruction_part = instruction[index]

            instruction_part = fill_binary_with_missing_zeros(instruction_part, total_bits)

            new_instruction.append(instruction_part)
        new_parse_tree.append(new_instruction)

    return new_parse_tree


def create_partition_tree(parse_tree):
    partition_tree = []

    for instruction in parse_tree:
        instruction_name = instruction[0]
        partition_tree.append(Instructions.get_word_partitioning(instruction_name))

    return partition_tree


def main():
    if len(sys.argv) < 2:
        print('Missing file to read')
        sys.exit(2)
    filename = sys.argv[1]

    parse_tree = create_parse_tree_from_file(filename)
    partition_tree = create_partition_tree(parse_tree)

    for line in parse_tree:
        print line

    parse_tree = add_opcode_to_parse_tree(parse_tree)

    parse_tree = convert_immediate_decimal_to_binary(parse_tree)
    parse_tree = convert_register_to_binary(parse_tree)
    parse_tree = add_missing_zeros(parse_tree, partition_tree)

    for line in parse_tree:
        print line
main()
