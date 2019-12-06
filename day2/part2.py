#!/usr/bin/env python
import itertools
import sys
from part1 import execute_intcode


def call_intcode(program, input1, input2):
    program = program[:]
    program[1:3] = input1, input2
    result = execute_intcode(program)
    return result[0]


MAX_NUM = 100


def brute_force_output(program, output):
    '''Try to brute force the inputs for program to achieve answer. Pair of
    inputs if answer found, or None.
    '''
    for in1, in2 in itertools.product(range(MAX_NUM), range(MAX_NUM)):
        if call_intcode(program, in1, in2) == output:
            return (in1, in2)
    else:
        return None


def main():
    fname = sys.argv[1]
    answer = int(sys.argv[2])

    with open(fname) as f:
        program = [int(code) for code in f.read().split(',')]

    result = brute_force_output(program, answer)

    if result:
        noun, verb = result
        print(f"noun={noun}, verb={verb}")
        print(f"100 * {noun} + {verb} = {100 * noun + verb}")
    else:
        print("Could not find answer.")


if __name__ == '__main__':
    main()
