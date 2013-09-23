import numbers
from numbers import Number

__author__ = 'fpaulo'

def main():
    x = 600851475143
    y = 2
    while x > 1:
        if x % y == 0:
            x /= y
        else:
            y += 1
    print y

if __name__ == "__main__":
    main()