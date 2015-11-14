def is_immediate_value(string):
    return '#' in string


def is_hex_number(number):
    return '0x' in number


def fill_binary_with_missing_zeros(binary, total_bits):
    return binary.zfill(total_bits)


def is_register(string):
    return 'r' in string
