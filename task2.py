from task1 import scrape_top_list
import json
file=open("task1.json","r")
data=json.load(file)

def group_by_year(movie):
    emp={}
    for i in data:
        top_movie_list=[]
        year=i["Year"]
        if year not in emp:
            for key in data:
                if year==key["Year"]:
                    top_movie_list.append(key)
            emp[year]=top_movie_list
    with open("task2.json","w+")as file:
        json.dump(emp,file,indent=4)
        a=json.dumps(emp)
group_by_year(scrape_top_list)


