import requests
import json
users_num=10
r=requests.get(f'https://randomuser.me/api/?results={users_num}')
j_data=r.json()
results=j_data["results"]


file=open('users.txt','a')

for i in results:
    if r.status_code==200:
        try:
            file.write(f'{i["name"]["first"]}  {i["gender"]}\n')
            file.close()
        except:
            continue
    else:
        continue





    # if r.status_code==200:
    #     file.write(f'salom ')
    #     file.write('/n')
    #     # file.write(f'{i["name"]["first"]}  {i["gender"]}  {i["location"]["country"]}') 
    #     file.close




# location=results[0]["location"]
# for i in location:
#     print(i)










# print(type(results))
# for i in results:
#     print(type(i))
#     print(i["gender"])

# gen=results["gender"]
# print(gen)



    # for i in range(4):
    #     data=requests.get("https://randomuser.me/api/")
    #     j_data=data.json()
        
    #     result=j_data["results"][0]
    #     gen=result["gender"]
    #     print(gen)



