import requests
import json
from task1 import scrape_top_list
from task4 import movies_detailes

movie=scrape_top_list()
ten_movies=movie[:10]
def get_movie_detailes():
    details=[]
    for i in ten_movies:
        # print(i["Url"])
        for j in i:
            # print(j)
            if j=="Url":
                details.append(movies_detailes(i["Url"]))
        print(details)
    with open("task5.json","w+") as file:
        json.dump(details,file,indent=4)           
    

get_movie_detailes()