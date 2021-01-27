import requests
import json


r=requests.get('https://api.exchangeratesapi.io/latest')
res_now=r.json()
rate=res_now["rates"]

r=requests.get('https://api.exchangeratesapi.io/2006-01-04')
res_1999=r.json()
rate99=res_1999["rates"]

file=open('data.json','a')
file.write( f'{rate["RUB"]}  {rate99["RUB"]} \n' )
file.close