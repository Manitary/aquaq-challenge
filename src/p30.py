from utils import get_input, submit


def score(cards: tuple[int, ...]) -> int:
    s = sum(cards)
    if s % 2:
        return s // 2 + 1
    return 0


def main() -> int:
    data = tuple(tuple(map(int, tuple(x))) for x in get_input(30).split("\n"))
    return sum(score(row) for row in data)


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(30, ANSWER)
