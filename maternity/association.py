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


def get_locations():
    """
    추후에 클래스로 변경될 경우에는
    클래스 내부의 변수를 넘겨주는 방식으로 변경되어야 한다

    일단은 TDD를 위해서 함수에서 클래스로 변경하는 과정을 기록한다.
    """
    locations = [
        '서울시', '인천시', '경기도', '강원도',
        '충청도', '경상도', '부산시', '전라도',
        '제주도',
    ]
    return locations
