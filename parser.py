import sys
from file_helper import FileHelper
from instructions import *
from util import *
from struct import pack


def create_parse_tree_from_file(file_helper):
    # Open program file
    parse_tree = []
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
        if not is_label(instruction[0]):
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


def convert_immediate_decimal_to_binary(parse_tree, partition_tree):
    new_parse_tree = []

    for i, instruction in enumerate(parse_tree):
        new_instruction = []

        for j, word in enumerate(instruction):
            if is_immediate_value(word):

                # Convert hex numbers to decimal
                if is_hex_number(word):
                    integer = int(word[3:], 16)
                else:
                    integer = int(word[1:])

                # Convert integer to 2s complement value
                binary = integer_to_2s_complement(integer, partition_tree[i][j][1])
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

        if not is_label(instruction_name):
            partition_tree.append(Instructions.get_word_partitioning(instruction_name))

    return partition_tree


# Create label map
# key = label name, value = address in binary
#
# returns parse_tree, label_map
def create_label_map(parse_tree):
    new_parse_tree = []
    label_map = {}

    number_of_labels = 0
    for i, instruction in enumerate(parse_tree):
        label = instruction[0]

        if is_label(label):
            # Remove . prefix on label names
            label = label[1:]

            label_map[label] = str(i - number_of_labels)
            number_of_labels += 1
            continue

        new_parse_tree.append(instruction)

    return new_parse_tree, label_map


def change_label_with_address(parse_tree, label_map):
    new_parse_tree = []

    for instruction in parse_tree:
        if len(instruction) == 2:
            label_name = instruction[1]
            if label_name in label_map:
                instruction[1] = '#' + str(int(label_map[label_name])*2)

        new_parse_tree.append(instruction)

    return new_parse_tree


def concat_parse_tree(parse_tree):
    instruction_words = []

    for instruction in parse_tree:
        word = ''

        for partition in instruction:
            word += partition

        instruction_words.append(word)

    return instruction_words


def write_all_instructions_to_bit_file(instructions, file_helper):
    file_helper.create_bit_file()

    for instruction in instructions:

        # Convert 8 bits to char and then write one char at a time
        for i in xrange(0, 4):
            char = chr(int(instruction[i*8:(i+1)*8], 2))
            file_helper.write_data_to_binary_file(char)

    file_helper.close_bit_file()
    print('Created bit file')


def create_coe_file(instruction_words, filename):
    file = open(filename + '.coe', 'w')

    file.write('MEMORY_INITIALIZATION_RADIX=2;\n')
    file.write('MEMORY_INITIALIZATION_VECTOR=\n')

    # Each instruction is 32 bits.
    # Split each instruction into 16 bits and then write to file
    for instruction in instruction_words:
        first_part = instruction[0:16]
        second_part = instruction[16:32]
        file.write(first_part + ',\n')
        file.write(second_part + ',\n')

    file.write('0000000000000000;\n')

    file.close()
    print('Created coe file')


def main():
    if len(sys.argv) < 2:
        print('Missing file to read')
        print('To use this script you must type:')
        print('python parser.py file.v3k')
        sys.exit(2)
    filename = sys.argv[1]

    file_helper = FileHelper(filename)

    parse_tree = create_parse_tree_from_file(file_helper)
    parse_tree, label_map = create_label_map(parse_tree)
    parse_tree = change_label_with_address(parse_tree, label_map)

    partition_tree = create_partition_tree(parse_tree)

    parse_tree = add_opcode_to_parse_tree(parse_tree)
    parse_tree = convert_immediate_decimal_to_binary(parse_tree, partition_tree)
    parse_tree = convert_register_to_binary(parse_tree)
    parse_tree = add_missing_zeros(parse_tree, partition_tree)

    instruction_words = concat_parse_tree(parse_tree)

    for instruction in instruction_words:
        hex_representation = '%0*X' % ((len(instruction) + 3) // 4, int(instruction, 2))
        print '0x' + hex_representation

    #write_all_instructions_to_bit_file(instruction_words, file_helper)
    create_coe_file(instruction_words, filename)

main()
