# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
from sklearn.feature_extraction.text import CountVectorizer

with open("train.json") as json_file:
    json_data = json.load(json_file)
#import and read train.json file    

cuisines = []
for i in json_data:
    cuisines.append(i["cuisine"])
cuisines = list(set(cuisines))
# gives a list of the cuisines
    
ing = []
for j in json_data:
    ing.append(j["ingredients"])
# this gives a list of lists    

alling = []
for k in ing:
    for l in k:
        alling.append(l)
unique_alling = list(set(alling))
print len(alling)
#list containing all the entries in ingredients of train.json        

str_alling = []
str_alling = [x.replace(' ','') for x in alling]

# Forcing the vocabulary attribute will help you achieve the 6714 count
vect = CountVectorizer(vocabulary = unique_alling, analyzer = 'word', ngram_range = (1, 1))
X = vect.fit_transform(str_alling)
fn = vect.get_feature_names()
print len(vect.vocabulary_)
#X = X.toarray()


#from collections import Counter
#counts = Counter(str_alling)
#print(counts)
#from sklearn.feature_extraction.text import TfidfVectorizer
#vect = TfidfVectorizer(input = str_alling, ngram_range = (1, 1), analyzer = 'word', min_df = 1)
#y = vect.fit_transform(str_alling)
#feature_names = vect.get_feature_names()

