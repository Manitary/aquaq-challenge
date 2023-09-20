from utils import get_input, submit


def main() -> int:
    data = tuple(map(int, get_input(40).strip().split()))
    peaks: dict[int, int] = {}
    valleys: dict[int, int] = {}
    for i, h in enumerate(data[1:-1], start=1):
        if data[i - 1] < h > data[i + 1]:
            peaks[i] = h
        elif data[i - 1] >= h <= data[i + 1]:
            valleys[i] = h
    prominences = 0
    for i, h in peaks.items():
        left_prominence, right_prominence = 0, 0
        left = max((il for il, hl in peaks.items() if il < i and hl >= h), default=0)
        if left:
            left_prominence = min(hv for iv, hv in valleys.items() if left < iv < i)
        right = min((il for il, hl in peaks.items() if il > i and hl >= h), default=0)
        if right:
            right_prominence = min(hv for iv, hv in valleys.items() if i < iv < right)
        prominence = h - max(left_prominence, right_prominence)
        prominences += prominence or h

    return prominences


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(40, ANSWER)
