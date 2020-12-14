import time
import json
from typing import List

from requests import Request, Response, Session
from bs4 import BeautifulSoup, Tag


def get_userid(path="./credentials.json") -> str:
    """
    Returns the user id read from [path].
    """
    with open(path, 'r', encoding='utf-8') as f:
        userid = json.load(f)["userid"]
    return userid


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


def flatten(inp: list) -> list:
    """
    Returns the flattened list.
    """
    return (lambda t: [item for sublist in t for item in sublist])(inp)


def get_weekday() -> int:
    """
    Returns 0~6 corresponding from Sunday to Saturday.
    """
    return int(time.strftime('%w'))
