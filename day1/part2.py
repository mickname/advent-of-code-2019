#!/usr/bin/env python
import sys


def fuel_required(mass):
    total_fuel = 0
    while True:
        required = mass // 3 - 2
        if required > 0:
            total_fuel += required
            mass = required
        else:
            return total_fuel


def main():
    with open(sys.argv[1]) as f:
        total_fuel = sum(fuel_required(int(l)) for l in f)

        print(f"Total fuel required: {total_fuel}")


if __name__ == '__main__':
    main()
