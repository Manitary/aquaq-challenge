from utils import get_input, submit


def count_ones(*nums: int) -> int:
    return sum(str(num).count("1") for num in nums)


def main() -> int:
    data = int(get_input(6).split()[-1])
    print(data)
    ans = 0
    for i in range(data + 1):
        for j in range(i, data + 1 - i):
            k = data - i - j
            if k < j:
                break
            ones = count_ones(i, j, k)
            s = len({i, j, k})
            if s == 3:
                ans += 6 * ones
            elif s == 2:
                ans += 3 * ones
            elif s == 1:
                ans += ones

    return ans


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(6, ANSWER)
