#-*- coding: utf-8 -*-

import re

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

"""
<section id="bo_v_atc">
<h2 id="bo_v_atc_title">본문</h2>
<div id="bo_v_img">
</div>
<!-- 본문 내용 시작 { -->
<div id="bo_v_con"><div><span style="font-size:19px;">주   소 : 서울 강남구 대치동 984 로얄빌딩 3층</span></div>
<div> </div>
<div><span style="font-size:19px;">전   화 : 02) 558-2053</span></div>
<div> </div>
<div><span style="font-size:19px;">홈페이지 : <a href="http://www.allobebe.kr/">http://www.allobebe.kr/</a></span></div>
<div> </div>
<div><span style="font-size:19px;"><a class="view_image" href="http://shjw.or.kr/bbs/view_image.php?fn=%2Fdata%2Feditor%2F1406%2F1982136337_1403246229.8641.jpg" target="_blank"><img alt="" src="http://shjw.or.kr/data/editor/1406/thumb-1982136337_1403246229.8641_600x363.jpg"/></a></span></div>
</div>
<!-- } 본문 내용 끝 -->
<!-- 스크랩 추천 비추천 시작 { -->
<!-- } 스크랩 추천 비추천 끝 -->
</section>
"""

address = re.search(
    '주.*소.*\n',
    contents.text.encode("UTF-8")).group(0).split(":")[-1].strip()

contact = re.search(
    '전.*화.*\n',
    contents.text.encode("UTF-8")).group(0).split(":")[-1].strip()

homepage = contents.find("a")["href"]
img_src = contents.find("img")["src"]

print(title)
print(address)
print(contact)
print(homepage)
print(img_src)
