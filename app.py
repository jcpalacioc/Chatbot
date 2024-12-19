import requests
import pandas as pd
import json

url=f'https://data.sec.gov/api/xbrl/companyfacts/CIK0001652044.json'

headers={'User-Agent':'palajnc@gmail.com'}

response=requests.get(url,headers=headers)
assets=pd.json_normalize(response.json())
            
try:
    response=requests.get(url,headers=headers)
    print(response)
    assets=pd.json_normalize(response.json()['units']['USD/shares'])
    #assets['ticker']=symbol_cik
except:
    pass
#full=pd.concat([full,assets],ignore_index=True,axis=0)
print(assets)

with open('company_data.json', 'w') as json_file: json.dump(response.json(), json_file, indent=4)



