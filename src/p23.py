from utils import get_input, submit

KEYWORD = "power plant"


def make_grid(keyword: str) -> tuple[tuple[str, ...], ...]:
    alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1) if chr(i) != "j"]
    ans = ""
    for c in keyword + "".join(alphabet):
        if c.isalpha() and c not in ans:
            ans += c
    return tuple(tuple(ans[i : i + 5]) for i in range(0, 25, 5))


def decrypt(grid: tuple[tuple[str, ...], ...], c1: str, c2: str) -> str:
    p1, p2 = (-1, -1), (-1, -1)
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == c1:
                p1 = (i, j)
            elif c == c2:
                p2 = (i, j)
    if (row := p1[0]) == p2[0]:
        return grid[row][(p1[1] - 1) % 5] + grid[row][(p2[1] - 1) % 5]
    if (col := p1[1]) == p2[1]:
        return grid[(p1[0] - 1) % 5][col] + grid[(p2[0] - 1) % 5][col]
    return grid[p1[0]][p2[1]] + grid[p2[0]][p1[1]]


def main() -> str:
    data = get_input(23)
    grid = make_grid(KEYWORD)
    return "".join(decrypt(grid, c1, c2) for c1, c2 in zip(data[::2], data[1::2]))


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(23, ANSWER)
