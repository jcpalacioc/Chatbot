import requests
import pandas as pd
import time
import warnings

class SEC_API:
    def __init__(self,tickers_eps=None):
        self.tickers_eps=tickers_eps
        self.tickers=self._connect_tickers()
        self.features={
            'accounts_payable_current':'AccountsPayableCurrent',
            'eps':'EarningsPerShareDiluted',
            'accounts_current_receivable':'AccountsPayableCurrent'
        }
    
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
    
    def _obtain_full_stats(self,tickers,stat):
        full=pd.DataFrame()
        assets=pd.DataFrame()
        headers={'User-Agent':'palajnc@gmail.com'}
        
        for i in range(len(tickers)):
            time.sleep(0.1)
            #print(i)
            symbol_cik=self.tickers.loc[tickers.index]["cik_str"].values[i]
            url=f'https://data.sec.gov/api/xbrl/companyconcept/{symbol_cik}/us-gaap/{stat}.json'
            
            try:
                response=requests.get(url,headers=headers)
                print(response)
                assets=pd.json_normalize(response.json()['units']['USD/shares'])
                assets['ticker']=symbol_cik
            except:
                pass
            full=pd.concat([full,assets],ignore_index=True,axis=0)

        full.rename(columns={'ticker':'cik_str'},inplace=True)
        full=full.merge(self.tickers,how='left',on='cik_str')
        return full
    
    def _obtain_quaterly(self,stats_df):
        interest_eps=stats_df[~stats_df['frame'].isna()]
        interest_eps['is_quaterly']=interest_eps['frame'].apply(lambda x: 'Q' in x)
        interest_eps=interest_eps[interest_eps['is_quaterly']==True]
        return interest_eps
    
    def obtain_feature_historical(self,tickers,stat='eps'):
        filtered_tick=self.tickers[self.tickers['ticker'].isin(tickers)]
        
        self.tickers_eps=self._obtain_full_stats(filtered_tick,self.features[stat])
        self.tickers_eps=self._obtain_quaterly(self.tickers_eps)
        
        return self.tickers_eps