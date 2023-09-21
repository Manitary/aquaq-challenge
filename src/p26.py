from utils import get_input, submit


def next_larger_permutation(n: str) -> str:
    l = list(n)
    for i in range(len(l) - 2, -1, -1):
        if all(x <= l[i] for x in l[i + 1 :]):
            continue
        tail = l[i:]
        head = min(x for x in tail[1:] if x > tail[0])
        tail.remove(head)
        return "".join(l[:i] + [head] + sorted(tail))
    return n


def main() -> int:
    data = get_input(26).split("\n")
    return sum(int(next_larger_permutation(d)) - int(d) for d in data)


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(26, ANSWER)
