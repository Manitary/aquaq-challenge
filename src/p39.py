from utils import get_input, submit


def main() -> int:
    data = tuple(map(int, get_input(39).split()))
    target = 501
    winning_darts = 0
    player = 0
    wins = [0, 0]
    leg_start = 0
    leg_count = 0
    scores = [0, 0]
    for s in data:
        scores[player] += s
        if scores[player] >= target:
            wins[player] += 1
            winning_darts += s
            scores = [0, 0]
            leg_count = 0
            leg_start = 1 - leg_start
            player = leg_start
            continue
        leg_count += 1
        if leg_count == 3:
            player = 1 - player
            leg_count = 0
    return winning_darts * wins[0]


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(39, ANSWER)
