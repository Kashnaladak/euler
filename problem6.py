__author__ = 'fpaulo'

import math


def sumSquareDifference(n):
    sumOfTheSquare = ((2 * math.pow(n,3)) + (3 * math.pow(n,2)) + n) / 6
    squareOfTheSum = math.pow(n * (n+1) / 2, 2)

    return squareOfTheSum - sumOfTheSquare


def main():
    print sumSquareDifference(100)


if __name__ == "__main__":
    main()