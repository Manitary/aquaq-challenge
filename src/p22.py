from utils import get_input, submit

NUM = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}


def to_roman(n: int) -> str:
    ans = ""
    for d, c in NUM.items():
        while n >= d:
            ans += c
            n -= d
    return ans


def main() -> int:
    data = tuple(map(int, get_input(22).split()))
    return sum(map(lambda c: ord(c) - 64, "".join(to_roman(n) for n in data)))


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(22, ANSWER)
