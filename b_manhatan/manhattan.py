from typing import List, Tuple
import bisect


def manhattan(points: List[Tuple[int, int]]) -> int:
    horizontals = {}  # key is Y, values is X
    verticals = {}  # key is X, values is Y
    horiz_keys = []
    vert_keys = []

    for x, y in points:
        verticals.setdefault(x, []).append(y)
        horizontals.setdefault(y, []).append(x)

    for x in verticals:
        verticals[x] = sorted(verticals[x])
    for y in horizontals:
        horizontals[y] = sorted(horizontals[y])

    vert_keys = sorted(verticals.keys())
    horiz_keys = sorted(horizontals.keys())

    paths = 0

    # print(f"verticals={verticals}")
    # print(f"horizontals={horizontals}")
    # print(f"vert_keys={vert_keys}")
    # print(f"horiz_keys={horiz_keys}")

    for i, x in enumerate(vert_keys):
        for j, y in enumerate(horiz_keys):
            h = horizontals[y]
            if x not in set(h):
                continue

            idx = bisect.bisect_right(h, x)
            to_right = h[idx:]
            for ir, xr in enumerate(to_right):
                v = verticals[xr]
                idx = bisect.bisect_left(v, y)
                to_bottom = v[:idx]
                for jb, yb in enumerate(to_bottom):
                    h2 = horizontals[yb]
                    idx = bisect.bisect_left(h2, xr)
                    to_left = h2[:idx]
                    for iu, xu in enumerate(to_left):
                        if xu == x:
                            paths += 1
                            # print(
                            #     f"({x}, {y}) ({xr}, {y}), ({xr}, {yb}), ({xu}, {yb})"
                            # )

    return paths


def test():
    def should_eq(expected, got):
        if expected != got:
            print(f"WRONG: expected={expected} got={got}")
            exit(-1)

    points = [
        (1, 1),
        (1, 7),
        (4, 7),
        (1, 5),
        (4, 5),
        (6, 5),
        (3, 3),
        (4, 1),
        (6, 7),
    ]
    should_eq(5, manhattan(points))

    points = [
        (-1, 1),
        (-1, 7),
        (-4, 7),
        (-1, 5),
        (-4, 5),
        (-6, 5),
        (-3, 3),
        (-4, 1),
        (-6, 7),
    ]
    should_eq(5, manhattan(points))

    points = [
        (1, -1),
        (1, -7),
        (4, -7),
        (1, -5),
        (4, -5),
        (6, -5),
        (3, -3),
        (4, -1),
        (6, -7),
    ]
    should_eq(5, manhattan(points))

    points = [
        (-1, -1),
        (-1, -7),
        (-4, -7),
        (-1, -5),
        (-4, -5),
        (-6, -5),
        (-3, -3),
        (-4, -1),
        (-6, -7),
    ]
    should_eq(5, manhattan(points))


def main():
    n = int(input())
    for i in range(n):
        k = int(input())
        points = []
        for k in range(k):
            x, y = map(lambda x: int(x), input().split(' '))
            points.append((x, y))
        n_paths = manhattan(points)
        print(n_paths)


if __name__ == "__main__":
    test()
    main()
