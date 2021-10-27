import random
import json
import time
with open ("task5.json","r+")as file:
    data=json.load(file)
movies=data
for i in movies:
    # print(i)
    random_time=random.randint(1,3)
    path=open("/home/dell/Desktop/Python/Web_Scraping/task9.text"+i["movie_name"]+"text","w")
    file=path.write(str(i))
    time.sleep(random_time)
    path.close()
























