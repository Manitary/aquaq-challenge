import csv
from typing import Hashable

from utils import get_input, submit


class Elo:
    def __init__(self, k: int) -> None:
        self._rating: dict[Hashable, float] = {}
        self._k = k

    def add_player(self, name: Hashable, rating: float = 1200) -> None:
        if name not in self._rating:
            self._rating[name] = rating

    def game_over(self, winner: Hashable, loser: Hashable) -> None:
        expected_result = self.expect_result(self._rating[winner], self._rating[loser])
        self._rating[winner] += self._k * (1 - expected_result)
        self._rating[loser] -= self._k * (1 - expected_result)

    def expect_result(self, p1: float, p2: float) -> float:
        return 1 / ((10.0 ** ((p2 - p1) / 400.0)) + 1)

    @property
    def rating(self) -> dict[Hashable, float]:
        return self._rating


def main() -> int:
    data = get_input(7).strip()
    contents = csv.DictReader(data.split("\n"))
    tournament = Elo(k=20)
    for row in contents:
        p1, p2 = row["h"], row["a"]
        tournament.add_player(p1)
        tournament.add_player(p2)
        score = tuple(map(int, row["score"].split("-")))
        if score[0] > score[1]:
            tournament.game_over(p1, p2)
        elif score[0] < score[1]:
            tournament.game_over(p2, p1)

    return int(max(tournament.rating.values())) - int(min(tournament.rating.values()))


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(7, ANSWER)
