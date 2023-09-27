from utils import get_input, submit

GRID = (
    (6, 17, 34, 50, 68),
    (10, 21, 45, 53, 66),
    (5, 25, 36, 52, 69),
    (14, 30, 33, 54, 63),
    (15, 23, 41, 51, 62),
)


def make_grid() -> list[list[int]]:
    return [[0] * len(GRID) for _ in range(len(GRID))]


def is_complete(grid: list[list[int]]) -> bool:
    if any(all(x for x in row) for row in grid):
        return True
    if any(all(x for x in col) for col in zip(*grid)):
        return True
    if all(grid[i][i] for i in range(len(grid))):
        return True
    if all(grid[i][len(grid) - i - 1] for i in range(len(grid))):
        return True
    return False


def play_round(calls: tuple[int, ...]) -> int:
    grid = make_grid()
    for turn, n in enumerate(calls):
        for i, row in enumerate(GRID):
            for j, x in enumerate(row):
                if x == n:
                    grid[i][j] = 1
                    if is_complete(grid):
                        return turn + 1
    return 0


def main() -> int:
    data = tuple(tuple(map(int, row.split())) for row in get_input(14).split("\n"))
    return sum(play_round(nums) for nums in data)


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(14, ANSWER)
