import re
from datetime import datetime
from typing import Sequence

from utils import get_input, submit

MORSE = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}
MORSE_REV = {v: k for k, v in MORSE.items()}

TICK_SYMBOL = {1: ".", 3: "-"}
TICK_SPACE = {1: "", 3: ",", 7: " "}


def parse_diffs(ticks: Sequence[int]) -> str:
    ans = ""
    word = ""
    chars = ""
    for i, t in enumerate(ticks):
        if i % 2 == 0:
            chars += TICK_SYMBOL[t]
            continue
        if t >= 3:
            word += MORSE_REV[chars]
            chars = ""
        if t == 7:
            ans += word + " "
            word = ""
    if word or chars:
        ans += word + MORSE_REV[chars]
    return ans


def parse_times(times: Sequence[str]) -> list[int]:
    times_converted: tuple[datetime, ...] = tuple(
        map(lambda t: datetime.strptime(t, "%H:%M:%S.%f"), times)
    )
    diffs = [
        int((b - a).total_seconds() * 1000)
        for a, b in zip(times_converted, times_converted[1:])
    ]
    tick = min(diffs)
    ans = [x // tick for x in diffs]
    return ans


def main() -> str:
    data = re.split(r"\n +\n", get_input(25))
    for times in data:
        ticks = parse_times(times.split("\n"))
        print(parse_diffs(ticks))
    # Need to read the messages to deduce the solution
    return "paris"


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(25, ANSWER)
