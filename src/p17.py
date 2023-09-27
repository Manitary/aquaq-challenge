import csv
from collections import defaultdict
from datetime import datetime

from utils import get_input, submit


class Team:
    def __init__(self) -> None:
        self.shames: list[tuple[datetime, datetime]] = []
        self.shame_start: datetime | None = None

    def update(self, date: datetime, goals: int) -> None:
        if goals and self.shame_start:
            self.shames.append((self.shame_start, date))
            self.shame_start = None
            return
        if not goals and not self.shame_start:
            self.shame_start = date

    @property
    def longest_shame_length(self) -> int:
        if not self.shames:
            return 0
        return max(s[1] - s[0] for s in self.shames).days

    @property
    def longest_shame_print(self) -> str:
        if not self.shames:
            return ""
        shame = max(self.shames, key=lambda s: s[1] - s[0])
        return " ".join(date.strftime("%Y%m%d") for date in shame)


def main() -> str:
    data = csv.DictReader(get_input(17).split("\n"))
    teams: dict[str, Team] = defaultdict(Team)
    for row in data:
        year, month, day = tuple(map(int, row["date"].split("-")))
        date = datetime(year=year, month=month, day=day)
        teams[row["home_team"]].update(date, int(row["home_score"]))
        teams[row["away_team"]].update(date, int(row["away_score"]))
    most_shame = max(teams, key=lambda t: teams[t].longest_shame_length)
    return f"{most_shame} {teams[most_shame].longest_shame_print}"


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(17, ANSWER)
