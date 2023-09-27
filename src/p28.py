from utils import get_input, submit

MESSAGE = "FISSION_MAILED"


def start_row(view: list[list[str]], c: str) -> int:
    return tuple(row[0] for row in view).index(c)


def move(view: list[list[str]], p: list[int], d: list[int]) -> None:
    if view[p[0]][p[1]] == "/":
        d[0], d[1] = -d[1], -d[0]
        view[p[0]][p[1]] = "\\"
    elif view[p[0]][p[1]] == "\\":
        d[0], d[1] = d[1], d[0]
        view[p[0]][p[1]] = "/"
    elif view[p[0]][p[1]] != " ":
        raise ValueError("Invalid cell")
    p[0] += d[0]
    p[1] += d[1]


def encrypt(view: list[list[str]], c: str) -> str:
    r = start_row(view, c)
    p = [r, 1]
    d = [0, 1]
    while view[p[0]][p[1]] in {" ", "/", "\\"}:
        move(view, p, d)
    return view[p[0]][p[1]]


def main() -> str:
    data = list(map(list, get_input(28).split("\n")))
    return "".join(encrypt(data, c) for c in MESSAGE)


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(28, ANSWER)
