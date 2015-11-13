import sys
from file_helper import FileHelper
from instructions import *


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

        parse_tree.append(instruction)
        line = file_helper.read_line()

    file_helper.close_program_file()
    return parse_tree


def add_opcode_to_parse_tree(parse_tree):
    new_parse_tree = []
    for instruction in parse_tree:
        instruction[0] = Instructions.get_opcode(instruction[0])
        new_parse_tree.append(instruction)

    return new_parse_tree


def is_immediate_value(string):
    return '#' in string


def convert_decimal_to_binary(decimal_number):
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


def is_register(string):
    return 'r' in string


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


def main():
    if len(sys.argv) < 2:
        print('Missing file to read')
        sys.exit(2)
    filename = sys.argv[1]

    parse_tree = create_parse_tree_from_file(filename)
    print(parse_tree)

    parse_tree = add_opcode_to_parse_tree(parse_tree)
    print(parse_tree)

    parse_tree = convert_immediate_decimal_to_binary(parse_tree)
    print(parse_tree)

    parse_tree = convert_register_to_binary(parse_tree)
    print(parse_tree)
main()
