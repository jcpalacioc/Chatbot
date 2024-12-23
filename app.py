import requests
import pandas as pd
import json
from SEC_API import SEC_API

#API SEC Para descargar Datos contables y financieros

sec_api=SEC_API()
sec_api.save_json('NVDA')



