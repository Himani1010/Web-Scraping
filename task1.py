import requests
from bs4 import BeautifulSoup
import json

page = requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
soup = BeautifulSoup(page.text,"html.parser")
def scrape_top_list():
    list = []
    div = soup.find("div",class_ = "body_main container")
    tbody = div.find("table",class_ = "table")
    tr = tbody.find_all("tr")
    ranking=0
    for i in tr:
        dict1 = {}
        td = i.find_all("td")
        for j in td:
            rank = i.find("td",class_ = "bold").get_text()[:-1]
            dict1["Rank"] = int(rank)
            Rating=i.find('span', class_="tMeterIcon tiny").get_text()[3:-2]
            dict1['Rating']=float(Rating)
            Reviews=i.find('td', class_="right hidden-xs").get_text()
            dict1['Reviews']=Reviews
            movie_name=i.find('a',class_="unstyled articleLink") ['href'][3:]
            dict1['Movie']=movie_name
            url=("https://www.rottentomatoes.com/m/"+movie_name)
            dict1['Url']=url
            year=i.find('a', class_="unstyled articleLink").text[-5:-1]
            dict1['Year']=year
        for k in dict1:
            if k!={}:
                if dict1 not in list:
                    list.append(dict1)
            else:
                break
    file=open("task1.json",'w')
    json.dump(list, file, indent=4)

    return list

scrapped=scrape_top_list()

# from first_task1 import scrape_top_list
# import json
# file=open("webscrap1.json","r")
# data=json.load(file)

# def group_by_year(movies):
#     emp={}
#     for i in data:
#         top_movie_list=[]
#         year=i["Year"]
#         if year not in emp:
#             for key in data:
#                 if year==key["Year"]:
#                     top_movie_list.append(key)
#             emp[year]=top_movie_list
#     with open("webscrap2.json","w+")as file:
#         json.dump(emp,file,indent=4)
#         a=json.dumps(emp)
#     return emp
# group_by_year(scrapped)








# 









# n=int(input("enter the number"))
# i=1
# a=[]
# while i<=n:
#     a.append([i])
#     i=i+1
# print(a)
