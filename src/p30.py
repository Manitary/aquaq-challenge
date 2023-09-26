import sys
from functools import cache
from typing import Generator

from utils import get_input, submit

sys.setrecursionlimit(3500)

Cards = tuple[int, ...]


@cache
def flip_card(input_cards: Cards, pos: int) -> Generator[Cards, None, None]:
    if input_cards[pos] != 1:
        raise ValueError("Flipping the card is not possible")
    cards = list(input_cards)
    if pos == 0:
        cards[1] = 1 - cards[1]
        yield tuple(cards[1:])
    elif pos == len(cards) - 1:
        cards[-2] = 1 - cards[-2]
        yield tuple(cards[:-1])
    else:
        cards[pos - 1] = 1 - cards[pos - 1]
        cards[pos + 1] = 1 - cards[pos + 1]
        yield tuple(cards[:pos])
        yield tuple(cards[pos + 1 :])


def all_flips(cards: Cards) -> Generator[tuple[Cards, ...], None, None]:
    for pos, val in enumerate(cards):
        if val != 1:
            continue
        yield tuple(flip_card(cards, pos))


@cache
def is_valid_hand(cards: Cards) -> bool:
    if not cards:
        return True
    if 1 not in cards:
        return False
    if cards == (1,):
        return True
    if any(is_valid_flip(*flip) for flip in all_flips(cards)):
        return True
    return False


def is_valid_flip(*flip: Cards) -> bool:
    return all(is_valid_hand(sub_flip) for sub_flip in flip)


def main() -> int:
    data = tuple(tuple(map(int, tuple(x))) for x in get_input(30).split("\n"))
    return sum(
        is_valid_flip(*flip_card(row, i))
        for row in data
        for i, c in enumerate(row)
        if c == 1
    )


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(30, ANSWER)
