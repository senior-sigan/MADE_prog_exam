from typing import List, Tuple
import math


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def n_ways(height) -> int:
    return int(2**(height - 1))


def c(n: int, k: int) -> int:
    nf = math.factorial(n)
    nf //= math.factorial(k)
    nf //= math.factorial(n-k)
    return int(nf)


def get_sum(tree: List[List[int]]) -> int:
    height = len(tree)
    s = 0
    for i, tier in enumerate(tree):
        for j, node in enumerate(tier):
            s += node * c(i, j) * n_ways(height-i)
    return s


def ruletka(tree: List[List[int]]) -> Tuple[int, int]:
    n = n_ways(len(tree))
    s = get_sum(tree)

    if s == 0:
        return 0, 1

    d = gcd(abs(n), abs(s))

    s = int(s // d)
    n = int(n // d)

    if n < 0:
        n *= -1
        s *= -1

    return s, n


def main():
    n = int(input())
    for i in range(n):
        height = int(input())
        tree = [
            list(map(lambda x: int(x), input().split(" ")))
            for j in range(height)
        ]
        n, m = ruletka(tree)
        print(f"{n} {m}")


def test():
    def should_eq(expected, got):
        if expected != got:
            print(f"WRONG: expected={expected} got={got}")
    print("TEST")

    should_eq((0, 1), ruletka([]))
    should_eq((5, 1), ruletka([[5]]))
    should_eq((0, 1), ruletka([[1], [-1, -1]]))
    should_eq((7, 2), ruletka([[1], [2, 3]]))
    should_eq((-6, 1), ruletka([[-2], [-2, -2], [-2, -2, -2]]))
    should_eq((9, 4), ruletka([[5], [-2, 3], [0, -7, 1]]))
    should_eq((17, 1), ruletka([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))
    res = ruletka(build_ruletka(63))
    print(res)

    exit(-1)


def build_ruletka(height):
    return [[1 for j in range(i+1)] for i in range(height)]


if __name__ == "__main__":
    # test()
    main()
