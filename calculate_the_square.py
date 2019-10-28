#!/usr/bin/env python3

# Created by: Jaeyoon Lee
# Created on: Oct 2019
# This program display square of 0 to user integer


def main():
    # this function uses a for loop

    # input
    integer = int(input("Enter the integer you want to calculate the square from 0: "))
    print("")

    # process & output
    for loop_counter in range(integer + 1):
        result = loop_counter ** 2
        print("{0}² = {1}".format(loop_counter, result))


if __name__ == "__main__":
    main()
