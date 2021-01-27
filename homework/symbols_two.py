import requests
import json

res=requests.get('https://api.exchangeratesapi.io/latest?symbols=EUR,USD')
res=res.json()
rates=res["rates"]


file=open('data.json','a')
file.write( f'{rates["USD"]   rates["EUR"]} \n' )
file.close
