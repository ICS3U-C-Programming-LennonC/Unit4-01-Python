#!/usr/bin/env python3
# Created By: Lennon Cehajic
# Date: November 13th, 2026
# This program calculates the sum  of all numbers.


def main():
    # Declare variables
    total = 0
    counter = 0

    # Get user input
    user_num = input("Enter a positive integer: ")

    # Try casting user input to int and check if number is positive
    try:
        user_int = int(user_num)

        if user_int < 0:
            print("Integer is not positive. Enter positive number.")

        else:
            while user_int >= counter:
                print("Tracking {} times through loop.".format(counter))
                total = total + counter
                counter = counter + 1

            print("The sum of the numbers from 0-{} is {}".format(user_int, total))

    except ValueError:
        print("{} is not a valid integer.".format(user_num))


if __name__ == "__main__":
    main()
