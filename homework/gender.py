
import requests
import json
users_num=10
r=requests.get(f'https://randomuser.me/api/?results={users_num}')
info=r.json()
results=info["results"]

for i in results:
    print(i["gender"])
    
