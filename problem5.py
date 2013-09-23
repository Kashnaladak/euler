__author__ = 'fpaulo'


def getMinMultiple():
    i = 10
    count = 0
    while True:

        for n in range(10,0,-1):
            if i % n != 0:
                break
            if n == 1:
                return i
        i += 20

        count += 1
        if count % 10000 == 0:
            print count

    return None


def main():
    print getMinMultiple()


if __name__ == "__main__":
    main()