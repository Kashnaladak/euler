__author__ = 'fpaulo'


def main():
    x = 1
    y = 2
    accum = 2
    while y < 4000000:
        y += x
        x = y - x
        if y % 2 == 0:
            accum += y
    print accum

if __name__ == "__main__":
    main()