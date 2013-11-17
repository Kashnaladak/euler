__author__ = 'fpaulo'


def getMinMultiple():
    interval = 20
    i = interval
    while True:

        for n in range(interval, 0, -1):
            if i % n != 0:
                break
            if n == 1:
                return i
        i += interval

    return None


def main():
    print getMinMultiple()


if __name__ == "__main__":
    main()