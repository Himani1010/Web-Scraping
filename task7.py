import json 
import requests
from bs4 import BeautifulSoup
with open ("task5.json","r+")as f2:
    data=json.load(f2)
def analyse_movies_directors(data):
    dic={}
    for i in data:
        if "director" in i:
            director=i["director"]
            # print(director)
            for j in director:
                if j not in dic:
                    director=j
                    dic[j]=1
                else:
                    dic[j]+=1
            else:
                continue

    # print(dic)
    with open ("task7.json","w+")as f1:
        json.dump(dic,f1,indent=5)

analyse_movies_directors(data)      