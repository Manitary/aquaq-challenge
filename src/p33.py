from functools import cache

from utils import get_input, submit

BASE_SCORES = list(range(1, 21))
DOUBLES = [2 * x for x in BASE_SCORES]
TRIPLES = [3 * x for x in BASE_SCORES]
BULLSEYE = [25, 50]
SCORES = sorted(list(set(BASE_SCORES + DOUBLES + TRIPLES + BULLSEYE)), reverse=True)


@cache
def min_darts_for(score: int) -> int:
    if not score:
        return 0
    return 1 + min(
        (min_darts_for(score - throw) for throw in SCORES if throw < score), default=0
    )


def main() -> int:
    data = int(get_input(33))
    return sum(min_darts_for(score) for score in range(1, data + 1))


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(33, ANSWER)
