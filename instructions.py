class Instructions(object):
    instructions = {
        'nop': {
            'opcode': '000000'
        },
        'jmp': {
            'opcode': '000001'
        },
        'mov': {
            'opcode': '000010'
        },
        'add': {
            'opcode': '000011'
        },
        'lsl': {
            'opcode': '000100'
        },
        'line': {
            'opcode': '000101'
        },
        'bezquad': {
            'opcode': '000110'
        },
        'bezqube': {
            'opcode': '000111'
        },
        'ldr': {
            'opcode': '001000'
        },
        'str': {
            'opcode': '001001'
        },
        'ldrp': {
            'opcode': '001010'
        },
        'strp': {
            'opcode': '001011'
        }
    }

    @staticmethod
    def get_opcode(instruction):
        value = Instructions.instructions[instruction]
        return value['opcode']
