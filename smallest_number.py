#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Oct 2021
# This program finds the smallest number in a list of 10 numbers

import random

import constants


def finding_smallest_number(random_numbers):
    # this function finds the smallest number

    lowest_number = random_numbers[9]

    for loop_counter in random_numbers:
        if loop_counter < lowest_number:
            lowest_number = loop_counter

    return lowest_number


def main():
    # this function calls other functions

    random_numbers = []

    # input
    print("Starting ...")
    print("\nHere is a list of random numbers: ")
    print("")

    # process
    for loop_counter in range(0, 10):
        a_random_number = random.randint(1, 100)  # a number between 1 and 100
        random_numbers.append(a_random_number)
        loop_counter1 = loop_counter + 1
        print(
            "The random number {0} is: {1}".format(
                loop_counter1, random_numbers[loop_counter]
            )
        )

    smallest_number = finding_smallest_number(random_numbers)

    print("")
    print("The smallest number is {0}.".format(smallest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
