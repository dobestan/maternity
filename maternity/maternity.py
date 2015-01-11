#-*- coding: utf-8 -*-

import requests
import bs4


def get_response(BASE_URL, params):
    response = requests.get(
        BASE_URL,
        params=params,
    )

    return response


BASE_URL = "http://shjw.or.kr/bbs/board.php"
params = {
    'bo_table': 'postnataldb',
    'sca': '서울시'
}
response = get_response(BASE_URL, params)

data = bs4.BeautifulSoup(response.text)
pages = int(
    data.find(
        "a",
        attrs={'class': 'pg_end'}
    )["href"].split("page=")[-1]
)
