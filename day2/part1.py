#!/usr/bin/env python
import operator
import sys


HALT_CODE = 99
opcodes = {
    1: operator.add,
    2: operator.mul,
}


def execute_intcode(program):
    program = program[:]
    program_counter = 0
    while True:
        opcode = program[program_counter]
        if opcode == HALT_CODE:
            return program
        pos1, pos2 = program[program_counter + 1:program_counter + 3]
        res = opcodes[opcode](program[pos1], program[pos2])
        program[program[program_counter + 3]] = res
        # Finally, increment pc
        program_counter += 4


def main():
    with open(sys.argv[1]) as f:
        program = [int(code) for code in f.read().split(',')]

    # "before running the program, replace position 1 with the value 12 and
    # replace position 2 with the value 2."
    program[1] = 12
    program[2] = 2

    result = execute_intcode(program)

    print(f"Value at position 0: {result[0]}")


if __name__ == '__main__':
    main()
