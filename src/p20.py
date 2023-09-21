from utils import get_input, submit

POINTS = (
    {str(x): {x} for x in range(2, 11)}
    | {"A": {1, 11}}
    | {x: {10} for x in ("J", "Q", "K")}
)


def main() -> int:
    data = get_input(20).split()
    wins = 0
    scores: set[int] = {0}
    for card in data:
        scores = {x + y for x in scores for y in POINTS[card]}
        if 21 in scores:
            wins += 1
            scores = {0}
            continue
        if all(x > 21 for x in scores):
            scores = {0}
            continue
        scores = {x for x in scores if x < 21}

    return wins


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(20, ANSWER)
