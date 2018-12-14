#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import os
import re
from pprint import pprint
from langdetect import detect_langs

# 한국어인지 아닌지 판단하는 함수 (한글 단어 임베딩 하려면 영어 데이터는
# 들어오면 안됨 )
def detect_kor(string):
    res = detect_langs(string)
    for item in res:
        if item.lang == "ko":
            return True
    return False

# 크롤링할때 html태그가 딸려오는데 그것을 지워주는 역할을 하는 함수

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    cleantext = cleantext.strip()
    cleantext = cleantext.replace('\n     ','').replace('\n','')
    cleantext = cleantext.replace('\t\t\t\t\t\t\t',' ')
    return cleantext

# 주어진 path에 해당하는 html 정보를 가져와서 cleanhtml함수로 깨끗히 하여
# 반환하는 함수

def get_cleanhtml(html_path, html_type = 'html'):
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    cleaned_data = []
    if html_type == 'html':
        data = soup.select(html_path)
        for datum in data:
            datum = cleanhtml(str(datum))
            cleaned_data.append(datum)
        return cleaned_data
    else:
        data = soup.select(html_path)
        for datum in data:
            datum = cleanhtml(str(datum['src']))
            cleaned_data.append(datum)
        return cleaned_data

# 해먹남녀 사이트에서 nutrition부분만 엿같이 뒀길래 따로 함수 만듬 

def get_nutrition(html_path, data_dict):
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    nutritions = soup.select(html_path)

    if nutritions is None or len(nutritions) < 5:
        data_dict['calories'] = str(0)
        data_dict['carbohydrate'] = str(0)
        data_dict['protein'] = str(0)
        data_dict['sodium'] = str(0)
        data_dict['fat'] = str(0)
    else:
        data_dict['calories'] = cleanhtml(nutritions[0]['data-text'])
        data_dict['carbohydrate'] = cleanhtml(nutritions[1]['data-text'])
        data_dict['protein'] = cleanhtml(nutritions[2]['data-text'])
        data_dict['sodium'] = cleanhtml(nutritions[4]['data-text'])
        data_dict['fat'] = cleanhtml(nutritions[3]['data-text'])


all_data_dict = []
all_eng_data_dict = []
id_index = 0

# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath("/home/soonmok/capstone/please_my_fridge/hamuk/data/"))
# 여기에 페이지 최대값 넣으면 됨
id = 5023

# 페이지를 돌면서 크롤링을 한다!
for page_numbers in range(5600, 5685):
    req = requests.get('https://haemukja.com/recipes/' + str(page_numbers))

    my_title = get_cleanhtml('div.top > h1')
    my_recipe = get_cleanhtml('div.btm > ul > li')
    if not my_title or my_recipe is None and detect_kor(my_title):
        pass

    else:
        data_dict = {}
        data_dict['url'] = get_cleanhtml("ol.lst_step > li > div.img-cover > img", 'img')
        data_dict['directions'] = get_cleanhtml("ol.lst_step > li > p")
        data_dict['categories'] = get_cleanhtml("div.box_tag > a")
        data_dict['ingredients'] = get_cleanhtml("ul.lst_ingrd > li")
        data_dict['title'] = get_cleanhtml("div.top > h1")[0]
        data_dict['components'] = get_cleanhtml("ul.lst_ingrd > li > span")
        data_dict['id'] = id
        id += 1
        get_nutrition('div.nutrition > ul > li', data_dict)
        id_index = id_index + 1
        print(id_index)
        print("=================================")
        print(data_dict)
        all_data_dict.append(data_dict)

# 제이슨 파일로 입력
with open(os.path.join(BASE_DIR, 'addition_recipe.json'), 'w+') as json_file:
    json.dump(all_data_dict, json_file, ensure_ascii=False, indent=4)


