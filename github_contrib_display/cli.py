from . import lib


def main() -> None:
    """GitHub contributions."""
    USERID = lib.get_userid()
    URL = f"https://github.com/{USERID}"

    res = lib.get_res(URL)
    soup = lib.BeautifulSoup(res.text, 'html.parser')
    lines = lib.get_lines(soup)

    contribs = lib.flatten(list(map(
        lib.get_data_count,
        lines
    )))
    contribs_last_7days = contribs[-7:]

    today = contribs_last_7days[-1]
    print(f"Contributions from the last 7 days: {' '.join(map(str, contribs_last_7days))}")
    if contribs_last_7days[-1] == 0:
        print("Work more! You have 0 contributions today.")
    else:
        print(f"You've been working hard! You have {today} contributions today.")
