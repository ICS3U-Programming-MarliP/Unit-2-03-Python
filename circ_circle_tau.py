#!/usr/bin/env python3
# Created by: Marli Peters
# Created on: Sep. 27, 2023
# This program calculates the circumference of a circle using tau with user input.
import constants


def main():
    # get the radius from the user
    radius = float(input("Enter radius of the circle (cm): "))

    # calculate circumference
    circumference = constants.TAU * radius

    # display circumference
    print("")
    print("Circumference = {} cm".format(circumference))


if __name__ == "__main__":
    main()
