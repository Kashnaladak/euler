__author__ = 'fpaulo'

def isPal(x):
    s = str(x)
    j = len(s) - 1
    i = 0

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True


def main():
    max = -1
    for i in range(1,1000,1):
        for j in range(1,1000,1):
            n = i * j
            if isPal(n) and n > max:
                max = n
    print max

if __name__ == "__main__":
    main()