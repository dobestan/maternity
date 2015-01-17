# -*- coding: utf-8 -*-
import re
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


def get_all_detail_page_url_in_location(location):
    """
    특정 지역에 있는 모든 페이지의 링크를 배열로 저장하여 반환한다.
    ( 예, 서울시에 있는 모든 산후조리원 페이지 )
    """
    BASE_URL = "http://shjw.or.kr/bbs/board.php"
    detail_pages = list()

    total_pages = get_total_pages(get_response())
    for page in range(1, total_pages+1):
        params = {
            'bo_table': 'postnataldb',
            'sca': location,
            'page': page,
        }
        response = requests.get(BASE_URL, params=params)

        data = BeautifulSoup(response.text)
        detail_pages_block = data.findAll("tr")[1::]

        for detail_page_block in detail_pages_block:
            detail_page = detail_page_block.findAll("a")[1]["href"]
            detail_pages.append(detail_page)

    return detail_pages


def get_detail_information(detail_page_url):
    response = requests.get(detail_page_url)
    data = BeautifulSoup(response.text)

    title = data.find("h1", attrs={'id': 'bo_v_title'}).text.strip()
    contents = data.find("section", attrs={'id': 'bo_v_atc',})

    address = re.search(
        '주.*소.*\n',
        contents.text.encode("UTF-8")
    ).group(0).split(":")[-1].strip()

    contact = re.search(
        '전.*화.*\n',
        contents.text.encode("UTF-8")
    ).group(0).split(":")[-1].strip()

    homepage = contents.find("a")["href"]
    img_src = contents.find("img")["src"]

    information = {
        "title": title,
        "address": address,
        "contact": contact,
        "homepage": homepage,
        "img_src": img_src,
    }
    return information
