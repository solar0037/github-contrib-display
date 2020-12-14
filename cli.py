import time
from typing import List

from requests import Request, Response, Session
from bs4 import BeautifulSoup, Tag


def get_res(url: str) -> Response:
    """
    Returns the response.
    """
    sess = Session()
    req = Request('GET', url)
    req = req.prepare()
    res = sess.send(req)
    return res


def get_lines(soup: BeautifulSoup) -> List[Tag]:
    """
    Returns the lines from the js-calendar-graph-svg tag.
    """
    return soup.select('svg > g > g', class_='js-calendar-graph-svg')


def get_data_count(tag: Tag) -> List[List[int]]:
    """
    Selects the data-count attribute from the line.
    """
    return list(map(
        lambda x: int(x.get('data-count')),
        tag.select('rect')
    ))


def flatten_list(inp: list) -> list:
    """
    Returns the flattened list.
    """
    return (lambda t: [item for sublist in t for item in sublist])(inp)


def get_weekday() -> int:
    """
    Returns 0~6 corresponding from Sunday to Saturday.
    """
    return int(time.strftime('%w'))


if __name__ == '__main__':
    """GitHub contributions."""
    URL = "https://github.com/solar0037"

    res = get_res(URL)
    soup = BeautifulSoup(res.text, 'html.parser')
    lines = get_lines(soup)

    contribs = flatten_list(list(map(
        get_data_count,
        lines
    )))
    contribs_last_7days = contribs[-7:]

    today = contribs_last_7days[-1]
    print(f"Contributions from the last 7 days: {' '.join(map(str, contribs_last_7days))}")
    if contribs_last_7days[-1] == 0:
        print("Work more! You have 0 contributions today.")
    else:
        print(f"You've been working hard! You have {today} contributions today.")
