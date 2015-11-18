class Instructions(object):
    instructions = {
        'nop': {
            'opcode': '000000',
            'word_partition': [(0, 32)]
        },
        'jmp': {
            'opcode': '000001',
            'word_partition': [(0, 6), (1, 26)]
        },
        'mov': {
            'opcode': '000010',
            'word_partition': [(0, 6), (1, 5), (2, 21)]
        },
        'add': {
            'opcode': '000011',
            'word_partition': [(0, 6), (1, 5), (2, 5), (3, 5), (4, 11)]
        },
        'lsl': {
            'opcode': '000100',
            'word_partition': [(0, 6), (1, 5), (2, 5), (3, 16)]
        },
        'line': {
            'opcode': '000101',
            'word_partition': [(0, 6), (1, 10), (2, 5), (3, 11)]
        },
        'bezquad': {
            'opcode': '000110',
            'word_partition': [(0, 6), (1, 10), (2, 5), (3, 5), (4, 6)]
        },
        'bezqube': {
            'opcode': '000111',
            'word_partition': [(0, 6), (1, 10), (2, 5), (3, 5), (4, 6)]
        },
        'ldr': {
            'opcode': '001000',
            'word_partition': [(0, 6), (1, 5), (2, 21)]
        },
        'str': {
            'opcode': '001001',
            'word_partition': [(0, 6), (1, 5), (2, 21)]
        },
        'ldrp': {
            'opcode': '001010',
            'word_partition': [(0, 6), (1, 26)]
        },
        'strp': {
            'opcode': '001011',
            'word_partition': [(0, 6), (1, 26)]
        },
        'beq': {
            'opcode': '001100',
            'word_partition': [(0, 6), (1, 5), (2, 5), (3, 16)]
        },
        'movu': {
            'opcode': '001101',
            'word_partition': [(0, 6), (1, 5), (2, 21)]
        },
        'movl': {
            'opcode': '001110',
            'word_partition': [(0, 6), (1, 5), (2, 21)]
        }
    }

    @staticmethod
    def get_opcode(instruction):
        value = Instructions.instructions[instruction]
        return value['opcode']

    @staticmethod
    def get_word_partitioning(instruction):
        value = Instructions.instructions[instruction]
        return value['word_partition']
