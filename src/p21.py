from utils import get_input, submit

WIDTH = 5


def main() -> int:
    data = [list(map(int, row.split())) for row in get_input(21).split("\n")]
    data = [
        [sum(row[i : i + WIDTH]) for i in range(len(row) - WIDTH + 1)] for row in data
    ]
    while len(data) > 1:
        last_row = [0] + data.pop() + [0]
        data[-1] = [
            x + max(last_row[i - 1 : i + 2]) for i, x in enumerate(data[-1], start=1)
        ]

    return max(data.pop())


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(21, ANSWER)
