import requests
import pandas as pd
import time
import warnings
import json

#Clase para obtener datos financieros de la SEC
class SEC_API:
    def __init__(self,tickers_eps=None):
        self.tickers_eps=tickers_eps
        self.tickers=self._connect_tickers()
        self.features={
            'accounts_payable_current':'AccountsPayableCurrent',
            'eps':'EarningsPerShareDiluted',
            'accounts_current_receivable':'AccountsPayableCurrent'
        }
    
    #Descarga los tickers de la SEC en su Forma CIK para luego consumirlos en la API
    def _connect_tickers(self,debug=False):
        print('Downloading tickers from the SEC API')
        zeros_mapper={5:'00000',6:'0000',7:'000',8:'00'}

        headers={'User-Agent':'palajnc@gmail.com'}
        tickers=requests.get('https://www.sec.gov/files/company_tickers.json',headers=headers)
        tickers=pd.json_normalize(pd.json_normalize(tickers.json(),max_level=0).values[0])
        tickers['cik_lenght']=tickers['cik_str'].astype(str).apply(len)
        tickers['zeros_lenght']=tickers['cik_lenght'].map(zeros_mapper)
        tickers['cik_str']=f'CIK'+tickers['zeros_lenght']+tickers['cik_str'].astype(str)
        
        if debug:
            tickers.head(10)
        return tickers
    
    
    #Guarda los datos financieros de una corporacion en un archivo JSON
    #Recibe el ticker de la corporacion
    #Guarda el archivo en el directorio actual con toda la informacion financiera historica de la corporacion
    def save_json(self,ticker):
        cik=self.tickers[self.tickers['ticker'].isin([ticker])]['cik_str'].values[0]
        url=f'https://data.sec.gov/api/xbrl/companyfacts/{cik}.json'
        headers={'User-Agent':'palajnc@gmail.com'}

        response=requests.get(url,headers=headers)
        assets=pd.json_normalize(response.json())
                    
        try:
            response=requests.get(url,headers=headers)
            print(response)
            assets=pd.json_normalize(response.json()['units']['USD/shares'])
        except:
            pass
        print(assets)

        with open(f'{ticker}.json', 'w') as json_file: json.dump(response.json(), json_file, indent=4)