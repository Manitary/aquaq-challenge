from functools import cache
from utils import get_input, submit


@cache
def flip_card(input_cards: tuple[int, ...], pos: int) -> frozenset[tuple[int, ...]]:
    if input_cards[pos] != 1:
        raise ValueError("Flipping the card is not possible")
    if len(input_cards) == 1:
        return frozenset()
    cards = list(input_cards)
    if pos == 0:
        cards[1] = 1 - cards[1]
        return frozenset({tuple(cards[1:])})
    if pos == len(cards) - 1:
        cards[-2] = 1 - cards[-2]
        return frozenset({tuple(cards[:-1])})
    cards[pos - 1] = 1 - cards[pos - 1]
    cards[pos + 1] = 1 - cards[pos + 1]
    return frozenset({tuple(cards[:pos]), tuple(cards[pos + 1 :])})


@cache
def all_flips(cards: tuple[int, ...]) -> set[frozenset[tuple[int, ...]]]:
    return {flip_card(cards, pos) for pos, val in enumerate(cards) if val == 1}


@cache
def is_valid(cards: frozenset[tuple[int, ...]]) -> bool:
    if not cards:
        return True
    if any(set(x) == {0} for x in cards):
        return False
    if any(
        all(
            not is_valid(flip)
            for flip in sorted(
                all_flips(sub), key=lambda f: min((len(x) for x in f), default=0)
            )
        )
        for sub in cards
    ):
        return False
    return True


def main() -> int:
    data = tuple(tuple(map(int, tuple(x))) for x in get_input(30).split("\n"))
    # data = ("11010", "110", "00101011010")
    # data = tuple(tuple(map(int, tuple(x))) for x in data)
    # print(data)
    ans = 0
    for j, row in enumerate(data):
        print(j)
        for i, c in enumerate(row):
            if c == 0:
                continue
            if is_valid(flip_card(row, i)):
                # print(row, i)
                ans += 1

    return ans


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(30, ANSWER)
