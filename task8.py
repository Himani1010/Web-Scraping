
import requests
import os
from task1 import scrape_top_list
data=scrape_top_list()
movies=data[:10]
def get_scrape_movie_details():
    for i in movies:
        path="/home/dell/Desktop/Python/Web_Scraping/8thfile.text"+i["Movie"]+"text"
        if os.path.exists(path):
            pass
        else:
            create=open("/home/dell/Desktop/Python/Web_Scraping/8thfile.text"+i["Movie"]+"text","w+")
            url=requests.get(i["Url"])
            c=create.write(url.text)
            create.close()
get_scrape_movie_details() 




























































































        
