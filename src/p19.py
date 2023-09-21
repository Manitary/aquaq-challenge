from itertools import product
from typing import Generator
from utils import get_input, submit


def ngbh(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    for i in (-1, 1):
        yield (x + i, y)
        yield (x, y + i)


def play_turn(board: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
    new_board = {
        (x, y): sum(board.get(coords, 0) for coords in ngbh(x, y)) % 2 for x, y in board
    }
    return new_board


def play_game(num_steps: int, size: int, *coords: int) -> int:
    board = {(x, y): 0 for x, y in product(range(size), repeat=2)}
    for x, y in zip(coords[::2], coords[1::2]):
        board[(x, y)] = 1
    for _ in range(num_steps):
        board = play_turn(board)
    ans = sum(board.values())
    print(num_steps, size, ans)
    return ans


def main() -> int:
    data = tuple(tuple(map(int, row.split())) for row in get_input(19).split("\n"))
    # data = [[int(x) for x in "350 6 2 2 2 3".split()]]
    return sum(play_game(*setup) for setup in data)


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    # submit(19, ANSWER)
