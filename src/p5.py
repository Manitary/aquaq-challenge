from utils import get_input, submit


class Die:
    __slots__ = ("front", "left", "top", "back", "right", "bottom", "opposite_sum")

    def __init__(self, front: int, left: int, top: int, opposite_sum: int = 7) -> None:
        self.opposite_sum = opposite_sum
        self.front = front
        self.left = left
        self.top = top

    def rotate_left(self) -> None:
        self.left, self.front = self.front, self.opposite_sum - self.left

    def rotate_right(self) -> None:
        self.left, self.front = self.opposite_sum - self.front, self.left

    def rotate_up(self) -> None:
        self.top, self.front = self.front, self.opposite_sum - self.top

    def rotate_down(self) -> None:
        self.top, self.front = self.opposite_sum - self.front, self.top

    def execute_instruction(self, instr: str) -> None:
        if instr == "U":
            self.rotate_up()
        elif instr == "D":
            self.rotate_down()
        elif instr == "L":
            self.rotate_left()
        elif instr == "R":
            self.rotate_right()
        else:
            raise ValueError(f"Invalid instruction: {instr}")

    @property
    def face(self) -> int:
        return self.front


def main() -> int:
    data = get_input(5)
    dice = (Die(1, 2, 3), Die(1, 3, 2))
    ans = 0
    for i, instr in enumerate(data):
        for d in dice:
            d.execute_instruction(instr)
        if dice[0].face == dice[1].face:
            ans += i
    return ans


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(5, ANSWER)
