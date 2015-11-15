class FileHelper(object):

    def __init__(self, filename):
        super(FileHelper, self).__init__()
        self.filename = filename

    def open_program_file(self):
        self.program_file = open(self.filename, 'r')

    def create_bit_file(self):
        self.bit_file = open(self.filename + '.bit', 'wb')

    def read_line(self):
        self.current_line = self.program_file.readline()
        return self.current_line

    def has_lines_left(self):
        return self.current_line != ''

    def write_data_to_binary_file(self, data):
        self.bit_file.write(data)

    def is_empty_line(self):
        return len(self.current_line) <= 1

    def close_bit_file(self):
        self.bit_file.close()

    def close_program_file(self):
        self.program_file.close()
