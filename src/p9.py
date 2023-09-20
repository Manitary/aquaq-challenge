from math import prod

from utils import get_input, submit


def main() -> int:
    return prod(map(int, get_input(9).strip().split("\n")))


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(9, ANSWER)
