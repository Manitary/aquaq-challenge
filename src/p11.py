import csv
import functools
import itertools

from utils import get_input, submit

Rect = tuple[int, ...]


def overlap(t1: Rect, t2: Rect) -> bool:
    dx = min(t1[2], t2[2]) - max(t1[0], t2[0])
    dy = min(t1[3], t2[3]) - max(t1[1], t2[1])
    return dx > 0 and dy > 0


def main() -> int:
    data = csv.reader(get_input(11).split("\n"))
    rectangles: tuple[Rect, ...] = tuple(
        tuple(map(int, row)) for i, row in enumerate(data) if i > 0
    )
    valid: set[Rect] = functools.reduce(
        set.union,
        (
            {t1, t2}
            for t1, t2 in itertools.combinations(rectangles, 2)
            if overlap(t1, t2)
        ),
    )
    return len(
        {(x, y) for t in valid for x in range(t[0], t[2]) for y in range(t[1], t[3])}
    )


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(11, ANSWER)
