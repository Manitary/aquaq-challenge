from pathlib import Path

import requests
from dotenv import dotenv_values

CONFIG: dict[str, str] = dotenv_values(".env")
INPUT_URL = "https://challenges.aquaq.co.uk/challenge/{num}/input.txt"


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
            f"Could not retrieve the page. Status code: {r.status_code}"
        )
    contents = r.text
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as f:
        f.write(contents)
    return contents
