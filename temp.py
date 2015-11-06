# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json

with open("train.json") as json_file:
    json_data = json.load(json_file)

cuisines = []
for i in json_data:
    cuisines.append(i["cuisine"])
cuisines = list(set(dol))
    
ingredients = []
for j in json_data:
    ingredients.append(j["ingredients"])

# Representing the list of unique ingredients for TF IDF processing
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

"""
 Note one thing. After making the TF IDF skeleton, 
 you should be fitting it on the proper data, not only
 on the unique set. Make sure you do that, only then 
 your results will be appropriate.
"""
from sklearn.feature_extraction.text import TfidfVectorizer
vect = TfidfVectorizer(input = str_alling, ngram_range = (1, 1), analyzer = 'word', min_df = 1)

# Here's your clue, change the following line.
y = vect.fit_transform(str_alling)
feature_names = vect.get_feature_names()
print y
