from utils import get_input, submit


def comfort_score(nums: tuple[int, ...], pos: int) -> int:
    n = len(nums)
    for l in range(1, n):
        s = 0
        for left in range(max(0, pos - l + 1), min(pos + 1, n - l + 1)):
            if left == max(0, pos - l + 1):
                s = sum(nums[left : left + l])
            else:
                s += nums[left + l - 1] - nums[left - 1]
            if s % l == 0:
                break
        else:
            return l - 1
    return n


def comfort_score_list(nums: tuple[int, ...]) -> int:
    return sum(comfort_score(nums, i) for i in range(len(nums)))


def main() -> int:
    data = tuple(tuple(map(int, row.split())) for row in get_input(38).split("\n"))
    return sum(comfort_score_list(row) for row in data)


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(38, ANSWER)
