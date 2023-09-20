from pathlib import Path

import requests
from dotenv import dotenv_values
from bs4 import BeautifulSoup, Tag

CONFIG: dict[str, str] = dotenv_values(".env")  # type:ignore
INPUT_URL = "https://challenges.aquaq.co.uk/challenge/{num}/input.txt"
SUBMIT_URL = "https://challenges.aquaq.co.uk/answer/{num}"
EXTRA_DATA = {
    37: "https://challenges.aquaq.co.uk/static/words.txt",
}


def get_input(num: int) -> str:
    """Get the input text of challenge num.

    Try to check the file from disk first.
    If it does not exist, request it from the website, then save it locally."""

    file_path = Path() / "inputs" / f"{num}.txt"
    if file_path.is_file():
        with file_path.open(encoding="utf-8") as f:
            contents = f.read()
            return contents
    print("path does not exist")
    r = requests.get(
        INPUT_URL.format(num=num),
        cookies={"session": CONFIG.get("SESSION_COOKIE", "")},
        timeout=60,
    )
    if not r.ok:
        raise ConnectionError(
            f"Failed to retrieve the page. Status code: {r.status_code}"
        )
    contents = r.text
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as f:
        f.write(contents)
    return contents


def submit(num: int, answer: str | int) -> None:
    r = requests.post(
        url=SUBMIT_URL.format(num=num),
        data={"answer": answer},
        cookies={"session": CONFIG.get("SESSION_COOKIE", "")},
        timeout=60,
    )
    if not r.ok:
        raise ConnectionError(
            f"Failed to submit the answer. Status code: {r.status_code}"
        )
    bs = BeautifulSoup(r.text, features="html.parser")
    containers = bs.find_all("div", "bd-container-body")
    for c in containers:
        assert isinstance(c, Tag)
        print(c.text.strip().split("\n")[0])


def get_additional_data(num: int) -> str:
    if num not in EXTRA_DATA:
        raise ValueError(f"Problem {num} does not have additional data")
    file_path = Path() / "inputs" / "extra" / f"{num}.txt"
    if file_path.is_file():
        with file_path.open(encoding="utf-8") as f:
            contents = f.read()
            return contents
    print("path does not exist")
    r = requests.get(
        EXTRA_DATA[num],
        cookies={"session": CONFIG.get("SESSION_COOKIE", "")},
        timeout=60,
    )
    if not r.ok:
        raise ConnectionError(
            f"Failed to retrieve the page. Status code: {r.status_code}"
        )
    contents = r.text
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as f:
        f.write(contents)
    return contents
