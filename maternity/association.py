# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def get_response():
    BASE_URL = "http://shjw.or.kr/bbs/board.php"
    params = {
        'bo_table': 'postnataldb',
        'sca': '서울시',
    }

    response = requests.get(BASE_URL, params=params)
    return response


def get_total_pages(response):
    data = BeautifulSoup(response.text)

    pages = int(
        data.find("a", attrs={'class': 'pg_end'})["href"].split("page=")[-1]
    )
    return pages
