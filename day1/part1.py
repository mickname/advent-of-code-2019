#!/usr/bin/env python
import sys


def main():
    with open(sys.argv[1]) as f:
        total_fuel = sum(int(l) // 3 - 2 for l in f)
        print(f"Total fuel required: {total_fuel}")


if __name__ == '__main__':
    main()
