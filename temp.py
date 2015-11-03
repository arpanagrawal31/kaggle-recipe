# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json

with open("train.json") as json_file:
    json_data = json.load(json_file)

dol = []
for i in json_data:
    dol.append(i["cuisine"])
dol = list(set(dol))
    
ing = []
for j in json_data:
    ing.append(j["ingredients"])

alling = []
for k in ing:
    for l in k:
        alling.append(l)
        
alling = list(set(alling))

str_alling = []
str_alling = [x.replace(' ','') for x in alling]

#from collections import Counter
#counts = Counter(str_alling)
#print(counts)
from sklearn.feature_extraction.text import TfidfVectorizer
vect = TfidfVectorizer(input = str_alling, ngram_range = (1, 1), analyzer = 'word', min_df = 1)
y = vect.fit_transform(str_alling)
feature_names = vect.get_feature_names()
print y
