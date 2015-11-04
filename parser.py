import sys
from file_helper import FileHelper
from instructions import *

def read_from_file(filename):
    #Open program file
    file_helper = FileHelper(filename)
    file_helper.open_program_file()

    line = file_helper.read_line()
    while file_helper.has_lines_left():
        instruction = line[:-1].split()

        if file_helper.is_empty_line():
            line = file_helper.read_line()
            continue

        opcode = Instructions.get_opcode(instruction[0])
        print(opcode)
        line = file_helper.read_line()

    file_helper.close_program_file()

def main():
    if len(sys.argv) < 2:
        print('Missing file to read')
        sys.exit(2)
    filename = sys.argv[1]

    read_from_file(filename)
main()
