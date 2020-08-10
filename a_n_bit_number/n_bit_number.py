import math


def progressia(n: int) -> int:
    return n*(n+1) / 2


def find_a(k: int) -> int:
    n = ((1+8*k)**0.5 - 1) / 2
    return int(math.ceil(n))


def find_b(k: int, a: int) -> int:
    p = progressia(a-1)
    b = (k-1) % p
    return int(b)


def n_bit_kth_number(k: int) -> int:
    if k == 1:
        return 3
    if k == 2:
        return 5
    if k == 3:
        return 6

    a = find_a(k)
    b = find_b(k, a)

    return (2**a + 2**b) % 35184372089371


def test():
    def should_eq(expected, got):
        if expected != got:
            print(f"WRONG: expected={expected} got={got}")
            exit(-1)

    should_eq(3, n_bit_kth_number(1))
    should_eq(5, n_bit_kth_number(2))
    should_eq(6, n_bit_kth_number(3))
    should_eq(9, n_bit_kth_number(4))
    should_eq(10, n_bit_kth_number(5))
    should_eq(12, n_bit_kth_number(6))
    should_eq(17, n_bit_kth_number(7))
    should_eq(18432, n_bit_kth_number(103))
    should_eq(13733871088263, n_bit_kth_number(10000))


def main():
    n_lines = int(input())
    for i in range(n_lines):
        k = int(input())
        num = n_bit_kth_number(k)
        print(num)


if __name__ == "__main__":
    test()
    main()
