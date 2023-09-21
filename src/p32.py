from utils import get_input, submit

BRACES = set("()[]{}")
CLOSE = {")": "(", "]": "[", "}": "{"}


def is_balanced(s: str) -> bool:
    stack: list[str] = []
    for c in s:
        if c not in BRACES:
            continue
        if c not in CLOSE:
            stack.append(c)
            continue
        if not stack or stack.pop() != CLOSE[c]:
            return False
    if stack:
        return False
    return True


def main() -> int:
    data = get_input(32).split("\n")
    return sum(is_balanced(row) for row in data)


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(32, ANSWER)
