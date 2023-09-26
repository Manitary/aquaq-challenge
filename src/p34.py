import csv
import enum
from dataclasses import dataclass
from typing import Sequence, ValuesView

from utils import get_input, submit


def clock_to_minute(clock: str) -> int:
    t = tuple(map(int, clock.split(":")))
    return t[0] * 60 + t[1]


class EventType(enum.Enum):
    ARRIVAL = 0
    DEPARTURE = 1


@dataclass
class TrainEvent:
    station: str
    timetable: int
    type: EventType
    time: int

    def delay(self, amount: int = 5) -> None:
        self.time += amount


class Route:
    def __init__(self) -> None:
        self.position = 0
        self.itinerary: list[TrainEvent] = []

    @property
    def station(self) -> str:
        return self.itinerary[self.position].station

    @property
    def current_event(self) -> TrainEvent:
        return self.itinerary[self.position]

    @property
    def current_time(self) -> int:
        return self.itinerary[self.position].time

    @property
    def next_time(self) -> int:
        return self.itinerary[self.position + 1].time

    @property
    def latest_event(self) -> EventType:
        return self.itinerary[self.position].type

    @property
    def next_event(self) -> EventType:
        return self.itinerary[self.position + 1].type

    @property
    def previous_station(self) -> str:
        if self.position in (0, 1):
            return ""
        return self.itinerary[
            self.position - (1 if self.latest_event == EventType.ARRIVAL else 2)
        ].station

    @property
    def is_active(self) -> bool:
        return self.position < len(self.itinerary) - 1

    @property
    def total_time(self) -> int:
        return self.itinerary[-1].time - self.itinerary[0].timetable

    def add_to_itinerary(self, station: str, timetable: int, delay: int = 5) -> None:
        new_time = (
            self.itinerary[-1].time + (timetable - self.itinerary[-1].timetable)
            if self.itinerary
            else timetable
        )
        arrival = TrainEvent(station, timetable, EventType.ARRIVAL, new_time)
        departure = TrainEvent(
            station, timetable, EventType.DEPARTURE, new_time + delay
        )
        self.itinerary.extend([arrival, departure])

    def wait(self, new_time: int) -> None:
        delay = new_time - self.current_time
        for i in range(self.position, len(self.itinerary)):
            self.itinerary[i].delay(delay)

    def advance(self) -> None:
        self.position += 1


class Planner:
    def __init__(self, route_names: Sequence[str]) -> None:
        self._routes = {name: Route() for name in route_names}

    @property
    def routes(self) -> ValuesView[Route]:
        return self._routes.values()

    @property
    def active_routes(self) -> set[Route]:
        return {r for r in self.routes if r.is_active}

    @property
    def longest_route_time(self) -> int:
        return max(r.total_time for r in self.routes)

    @property
    def view(self) -> dict[str, TrainEvent]:
        return {name: route.current_event for name, route in self._routes.items()}

    def route(self, route_name: str) -> Route:
        return self._routes[route_name]

    def execute(self) -> None:
        while self.active_routes:
            self.take_action()

    def take_action(self) -> None:
        next_time = min(route.next_time for route in self.active_routes)
        departing = {
            route
            for route in self.active_routes
            if route.next_time == next_time and route.next_event == EventType.DEPARTURE
        }
        if departing:
            self.do_departure(departing)
            return
        arriving = {
            route
            for route in self.active_routes
            if route.next_time == next_time and route.next_event == EventType.ARRIVAL
        }
        self.do_arrivals(arriving)

    def do_departure(self, routes: set[Route]) -> None:
        departing = min(routes, key=lambda r: r.previous_station)
        new_time = departing.next_time
        departing.advance()
        delayed = {
            r
            for r in self.active_routes
            if r.station == departing.station and r.next_event == EventType.DEPARTURE
        }
        for r in delayed:
            r.wait(new_time)

    def do_arrivals(self, routes: set[Route]) -> None:
        for r in routes:
            r.advance()


def main() -> int:
    data = get_input(34).split("\n")
    #     data = """station,r1,r2,r3
    # a,00:01,,00:02
    # b,00:16,,00:17
    # c,,00:21,
    # d,00:46,00:51,00:47""".split(
    #         "\n"
    #     )
    planner = Planner(data[0].split(",")[1:])
    table = csv.DictReader(data)
    for row in table:
        station = row["station"]
        for route, planned_time in row.items():
            if route == "station":
                continue
            if not planned_time:
                continue
            planner.route(route).add_to_itinerary(
                station, clock_to_minute(planned_time)
            )
    planner.execute()
    return planner.longest_route_time


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    # submit(34, ANSWER)
