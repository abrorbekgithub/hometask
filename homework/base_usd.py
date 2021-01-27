import requests
import json

res=requests.get('https://api.exchangeratesapi.io/latest?base=USD')
res=res.json()
rates=res["rates"]


file=open('data.json','a')
file.write( f'{ rates["USD"] rates["EUR"] rates["GBP"] } \n' )
file.close

