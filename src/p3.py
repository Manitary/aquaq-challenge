from typing import Iterable
from utils import get_input, submit

BOARD = (
    "  ##  ",
    " #### ",
    "######",
    "######",
    " #### ",
    "  ##  ",
)

MOVE = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


def create_map(board: Iterable[str] = BOARD) -> set[tuple[int, int]]:
    return {
        (r, c)
        for r, row in enumerate(board)
        for c, cell in enumerate(row)
        if cell == "#"
    }


def main() -> int:
    data = get_input(3).strip()
    area = create_map()
    pos = (0, 2)
    ans = 0
    for d in data:
        new_pos = tuple(map(sum, zip(pos, MOVE[d])))
        if new_pos in area:
            pos = new_pos
        ans += sum(pos)

    return ans


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(3, ANSWER)
