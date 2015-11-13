class Instructions(object):
    instructions = {
        'add': {
            'opcode': '100000000'
        },
        'scene': {
            'opcode': '11000000'
        },
        'mov': {
            'opcode': '11100000'
        }
    }

    @staticmethod
    def get_opcode(instruction):
        value = Instructions.instructions[instruction]
        return value['opcode']
