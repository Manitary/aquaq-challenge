from utils import get_input, submit

KEYPAD = {
    1: "",
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
    0: " ",
}


def main() -> str:
    data = (tuple(map(int, row.split())) for row in get_input(0).strip().split("\n"))
    return "".join(
        KEYPAD[button][(num - 1) % len(KEYPAD[button])] for button, num in data
    )


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(0, ANSWER)
