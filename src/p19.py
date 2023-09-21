import numpy as np
from numpy.typing import NDArray

from utils import get_input, submit


def play_turn(board: NDArray[np.int64]) -> NDArray[np.int64]:
    new_board = (
        sum(
            (np.roll(board, i, j) for i in (-1, 1) for j in (0, 1)),
            start=np.zeros(shape=board.shape, dtype=np.int64),
        )
        % 2
    )
    for i in (0, -1):
        new_board[i] = 0
        new_board[:, i] = 0
    return new_board


def play_game(num_steps: int, size: int, *coords: int) -> int:
    board = np.zeros((size + 2, size + 2), dtype=np.int64)
    for x, y in zip(coords[::2], coords[1::2]):
        board[x + 1, y + 1] = 1
    for _ in range(num_steps):
        board = play_turn(board)
    return int(np.sum(board))


def main() -> int:
    data = tuple(tuple(map(int, row.split())) for row in get_input(19).split("\n"))
    return sum(play_game(*setup) for setup in data)


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(19, ANSWER)
