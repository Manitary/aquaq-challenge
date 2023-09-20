import re

from utils import get_input, submit


def main() -> int:
    data = get_input(13).strip().split("\n")
    pattern = re.compile(r"(.*?)(\w\w*?)\2{2,}(.*?)")
    # \2{2,} fails in cases like "aab", but they do not appear in the input
    # \2{1,} failed at least for the case of "drjmxnisyvgufwbtzaahahahahahahahahahahahahahahahahahahahah"
    # as it picks up the "aa" in the middle before the 'true' repeating pattern "ah"
    ans = 0
    for word in data:
        match = pattern.fullmatch(word)
        if not match:
            raise ValueError("No repeated pattern found")
        num = (len(word) - len(match.group(1)) - len(match.group(3))) // len(
            match.group(2)
        )
        ans += num
    return ans


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(13, ANSWER)
