import numpy as np
import pandas as pd
from pymongo import MongoClient
import os
from sklearn.metrics import mean_squared_error
import tensorflow as tf
from langdetect import detect_langs
import re
import json

def detect_kor(string):
    res = detect_langs(string)
    for item in res:
        if item.lang == "ko":
            return True
    return False

def clean_str(string):
    re.sub(r)
client = MongoClient("mongodb://admin:avengers@210.89.190.82/please_my_fridge")
db = client['please_my_fridge']
#client = MongoClient('mongodb://root:avengers@210.89.190.82', 27017)
#client = MongoClient('ds119049.mlab.com', 19049)

print("connecting collections")
#db = client['please_my_fridge']
#db.authenticate(os.environ["mongoID"], os.environ["mongoPW"])
#db.authenticate("admin","avengers")
recipes = db.recipe_data

# data preprocessing
print("Starting Data Process")
components = []
for i, recipe in enumerate(recipes.find()):
    try:
        if recipe["conponents"]:
            for component in recipe["conponents"]:
                #print(recipe["conponents"])
                component = re.sub(r'\(.*\)', '', component)
                component = re.sub(r'\[.*\]', '', component)
                component = component.replace("&lt;", '')
                component = component.replace("&gt;", '')
                component = component.replace("&amp;", '')
                if detect_kor(component) and component not in components:
                    components.append(component)
                    print(component)
    except:
        pass

