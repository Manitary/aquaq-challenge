import numpy as np
from numpy.typing import NDArray

from utils import get_input, submit


def play_turn(board: NDArray[np.int64]) -> NDArray[np.int64]:
    new_board = np.pad(board, ((1, 1), (1, 1)))
    return (
        sum(
            (np.roll(new_board, i, j) for i in (-1, 1) for j in (0, 1)),
            start=np.zeros(shape=new_board.shape, dtype=np.int64),
        )
        % 2
    )[1:-1, 1:-1]


def play_game(num_steps: int, size: int, *coords: int) -> int:
    board = np.zeros((size, size), dtype=np.int64)
    for x, y in zip(coords[::2], coords[1::2]):
        board[x, y] = 1
    for _ in range(num_steps):
        board = play_turn(board)
    ans = np.sum(board)
    return int(ans)


def main() -> int:
    data = tuple(tuple(map(int, row.split())) for row in get_input(19).split("\n"))
    return sum(play_game(*setup) for setup in data)


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(19, ANSWER)
