from utils import get_input, submit

HEX = "0123456789abcdef"


def main() -> str:
    data = get_input(1)
    data += " " * ((3 - (len(data) % 3)) % 3)
    data = "".join(c if c in HEX else "0" for c in data)
    return "".join(
        data[i * (len(data) // 3) : i * (len(data) // 3) + 2] for i in range(3)
    )


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(1, ANSWER)
