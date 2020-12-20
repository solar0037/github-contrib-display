from typing import List
from . import lib


def main() -> None:
    """GitHub contributions."""
    # constants
    USERID = lib.get_userid()
    URL = f"https://github.com/{USERID}"

    # get response and parse lines
    res = lib.get_res(URL)
    soup = lib.BeautifulSoup(res.text, 'html.parser')
    lines = lib.get_lines(soup)

    # parse contribs
    contribs: List[int] = lib.flatten(list(map(
        lib.get_data_count,
        lines
    )))
    # avoid empty lists
    if not len(contribs):
        print("You don't have enough contributions.")
        exit(0)

    # get contribs from last 7 days
    contribs_last_7days = contribs[-7:]
    today = contribs_last_7days[-1]

    print(f"Contributions from the last 7 days: {' '.join(map(str, contribs_last_7days))}")
    if not contribs_last_7days[-1]:
        print("Work more! You have 0 contributions today.")
    else:
        print(f"You've been working hard! You have {today} contributions today.")
