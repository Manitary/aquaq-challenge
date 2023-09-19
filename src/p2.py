from utils import get_input, submit


def main() -> int:
    data = list(map(int, get_input(2).strip().split()))
    i = 0
    while i < len(data):
        try:
            idx = data[:i:-1].index(data[i])
            data = data[: i + 1] + (data[-idx:] if idx else [])
        except ValueError:
            i += 1
    return sum(data)


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(2, ANSWER)
