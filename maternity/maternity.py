#-*- coding: utf-8 -*-

import requests
import bs4


def get_response(BASE_URL, params={}):
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

"""
for page in range(1, pages+1):
    response = get_response(
        BASE_URL,
        {
            'bo_table': 'postnataldb',
            'sca': '서울시',
            'page': page,
        }
    )
"""

"""
response = get_response(
    BASE_URL,
    {
        'bo_table': 'postnataldb',
        'sca': '서울시',
        'page': 1,
    }
)

data = bs4.BeautifulSoup(response.text)
care_centers = data.findAll("tr")[1::]

for care_center in care_centers:
    detail_page = care_center.findAll("a")[1]["href"]
"""

response = get_response("http://shjw.or.kr/bbs/board.php?bo_table=postnataldb&wr_id=314&sca=%EC%84%9C%EC%9A%B8%EC%8B%9C&page=1")
data = bs4.BeautifulSoup(response.text)

information = {}

title = data.find(
    "h1",
    attrs={
        'id': 'bo_v_title'
    }
).text.strip()

contents = data.find(
    "section",
    attrs={
        'id': 'bo_v_atc',
    },
)
