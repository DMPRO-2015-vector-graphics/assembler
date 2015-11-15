def is_immediate_value(string):
    return '#' in string


def is_hex_number(number):
    return '0x' in number


def fill_binary_with_missing_zeros(binary, total_bits):
    return binary.zfill(total_bits)


def is_register(string):
    return 'r' in string


def is_label(string):
    return '.' in string


def integer_to_2s_complement(integer, number_of_bits):
    integer &= (2 << number_of_bits-1)-1 # mask
    formatStr = '{:0'+str(number_of_bits)+'b}'
    ret =  formatStr.format(int(integer))
    return ret