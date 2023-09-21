import csv

from utils import get_input, submit


class Milk:
    def __init__(self, amount: int, expire_in: int = 5) -> None:
        self.amount = amount
        self.expire_in = expire_in

    def drink(self, amount: int) -> None:
        self.amount -= amount

    def get_older(self) -> None:
        self.expire_in -= 1

    @property
    def is_expired(self) -> bool:
        return self.expire_in <= 0


class Storage:
    def __init__(self, daily_milk: int = 100, daily_cereals: int = 100) -> None:
        self.cereals = 0
        self.milk: list[Milk] = []
        self.daily_milk = daily_milk
        self.daily_cereals = daily_cereals

    @property
    def enough_cereals(self) -> bool:
        return self.cereals >= self.daily_cereals

    @property
    def enough_milk(self) -> bool:
        return bool(self.milk and (self.milk[0].amount >= self.daily_milk))

    @property
    def total_milk(self) -> int:
        return sum(milk.amount for milk in self.milk)

    @property
    def total_contents(self) -> int:
        return self.cereals + self.total_milk

    def breakfast(self) -> None:
        if self.enough_cereals and self.enough_milk:
            self.cereals -= self.daily_cereals
            self.milk[0].drink(self.daily_milk)

    def store_cereals(self, amount: int) -> None:
        self.cereals += amount

    def store_milk(self, milk: Milk) -> None:
        self.milk.append(milk)

    def remove_expired(self) -> None:
        while self.milk and self.milk[0].is_expired:
            self.milk.pop(0)

    def daily_routine(
        self, bought_cereals: int = 0, bought_milk: Milk | None = None
    ) -> None:
        for milk in self.milk:
            milk.get_older()
        if bought_cereals:
            self.store_cereals(bought_cereals)
        self.breakfast()
        if bought_milk:
            self.store_milk(bought_milk)
        self.remove_expired()


def main() -> int:
    data = get_input(8)
    contents = csv.DictReader(data.split("\n"))
    storage = Storage()
    for day in contents:
        cereals = int(day["cereal"])
        milk = int(day["milk"])
        storage.daily_routine(
            bought_cereals=cereals,
            bought_milk=Milk(milk) if milk else None,
        )
    return storage.total_contents


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(8, ANSWER)
