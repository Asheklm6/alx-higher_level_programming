#!/usr/bin/python3


def perm(str, p):
    d = {}

    n = len(p)
    N = len(str)
    for chr in p:
        d[chr] = 1

    start, matches = 0, 0

    for end in range(N):
        if str[end] in d:
            d[str[end]] -= 1
            if d[str[end]] == 0:
                matches += 1

        if matches == len(d):
            return True
        if end >= len(p):
            if (str[start]) in d:
                if d[str[start]] == 0:
                    matches -= 1
                d[str[start]] += 1
        start += 1
    return False


if __name__ == "__main__":
    print(perm("aaacbacarb", "abc"))
