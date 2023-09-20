import csv
from collections import defaultdict
from functools import partial
from typing import Callable

from utils import get_additional_data, get_input, submit

Rule = Callable[[str], bool]

WORDS = {word for word in get_additional_data(37).strip().split("\n") if len(word) == 5}


def convert(c: str) -> int:
    return ord(c) - 97


def exclude_if_not_enough_char(word: str, char: str, min_amount: int) -> bool:
    return word.count(char) < min_amount


def exclude_if_not_exact_num_char(word: str, char: str, amount: int) -> bool:
    return word.count(char) != amount


def exclude_if_has_char(word: str, char: str) -> bool:
    return char in word


def exclude_if_exact_char(word: str, char: str, pos: int) -> bool:
    return word[pos] == char


def exclude_if_not_exact_char(word: str, char: str, pos: int) -> bool:
    return word[pos] != char


def make_rules(guess: str, result: tuple[int, ...]) -> set[Rule]:
    rules_dict: dict[str, list[tuple[int, int]]] = defaultdict(list)
    for i, c in enumerate(guess):
        rules_dict[c].append((i, result[i]))
    exclusion_rules: set[Callable[[str], bool]] = set()
    for c, r in rules_dict.items():
        n = sum(x[1] > 0 for x in r)
        z = any(x[1] == 0 for x in r)
        if n:
            if z:
                exclusion_rules.add(
                    partial(exclude_if_not_exact_num_char, char=c, amount=n)
                )
            else:
                exclusion_rules.add(
                    partial(exclude_if_not_enough_char, char=c, min_amount=n)
                )
        elif z:
            exclusion_rules.add(partial(exclude_if_has_char, char=c))

        for s in r:
            i, v = s
            if v in {0, 1}:
                exclusion_rules.add(partial(exclude_if_exact_char, char=c, pos=i))
            elif v == 2:
                exclusion_rules.add(partial(exclude_if_not_exact_char, char=c, pos=i))

    return exclusion_rules


def apply_rule(candidates: set[str], rule: Rule) -> set[str]:
    return {word for word in candidates if not rule(word)}


def main() -> int:
    data = csv.DictReader(get_input(37).strip().split("\n"))
    candidates = WORDS
    answer = 0
    for row in data:
        for rule in make_rules(row["guess"], tuple(map(int, row["result"].split()))):
            candidates = apply_rule(candidates, rule)
        if len(candidates) == 1:
            answer += sum(map(convert, candidates.pop()))
            candidates = WORDS
    return answer


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(37, ANSWER)
