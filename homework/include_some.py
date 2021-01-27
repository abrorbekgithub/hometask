import requests
import json
users_num=10
r=requests.get(f'https://randomuser.me/api/?results={users_num}')
info=r.json()
results=info["results"]

for i in results:
    try:
        file=open('data.json','a')
        file.write( f'{ i["name"]["first"]}  {i["name"]["last"]}  {i["gender"]}  {i["dob"]["age"]}  {i["location"]["city"]}  {i["nat"]}  {i["phone"]}  {i["email"] } \n' )
        file.close
    except:
        continue