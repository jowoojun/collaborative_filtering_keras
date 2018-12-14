import json
import os
from langdetect import detect_langs
from pprint import pprint

def detect_kor(string):
    try:
        res = detect_langs(string)
        for item in res:
            if item.lang == "ko":
                return True
        return False
    except:
        return False

with open('profile_with_null.json') as f:
    items = json.load(f)

f.close()

BASE_DIR = os.path.dirname(os.path.abspath("/home/soonmok/capstone/please_my_fridge/hamuk"))

counter = 0
for item in items:
    counter += 1
    print(counter)
    new_scraps = []
    for scrap in item['scrap']:
        if scrap and detect_kor(scrap):
            new_scraps.append(scrap)
    item['scrap'] = new_scraps

with open(os.path.join(BASE_DIR, 'new_profile_with_null.json'), 'w+') as json_file:
    json.dump(items, json_file, ensure_ascii=False, indent=4)

json_file.close()
