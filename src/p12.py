from utils import get_input, submit


def main() -> int:
    data = tuple(
        map(lambda x: tuple(map(int, x.split())), get_input(12).strip().split("\n"))
    )
    max_floor = len(data) - 1
    curr_floor = 0
    visited = 1
    d = 1
    while 0 <= curr_floor <= max_floor:
        dc, n = data[curr_floor]
        d = d if dc else -d
        curr_floor += d * n
        visited += 1
    return visited


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(12, ANSWER)
