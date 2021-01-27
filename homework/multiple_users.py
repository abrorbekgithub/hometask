import requests
import json
users_num=10
r=requests.get(f'https://randomuser.me/api/?results={users_num}')
info=r.json()
results=info["results"]

for i in results:
    try:
        if r.status_code==200:
            file=open('data.json','a')
            file.write( f'{ i["name"]} \n' )
            file.close
        else:
            continue 
    except:
        continue   
