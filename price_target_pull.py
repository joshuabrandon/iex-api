import pandas as pd
import json
from urllib.request import urlopen

def call_url(method_url):
    """Base URL with personal auth token for call to IEX Cloud API.
    
    Keyword arguments:
    - method_url: the specific method URL snippet for the data pull
    
    Returns:
    - call_url: the URL used for the API call
    """
    # Token is stored privately in another file
    tokenFile = open('token.txt', 'r')
    token = tokenFile.readline()
    token_url = '?token=' + token
    
    # URL is a concatenation of the Base URL + Method URL + Auth Token
    call_url = 'https://cloud.iexapis.com/beta' + method_url + token_url
    
    return call_url

def price_target_call(symbol_list):
    """Returns analyst price targets for specified list of tickers.
    
    Keyword arguments:
    - symbol_list: a list of tickers; type = list of strings
    
    Returns:
    - df: high, low, and average price targets for list of tickers; tpye = Pandas DataFrame
    """
    # Initialize empty list for API URL calls and returned JSON data
    url = []
    data = []
    
    # Each API call is made seperately, loop on all tickers in the list and store returned JSON in a list
    for symbol in symbol_list:
        method_url = '/stock/' + symbol + '/price-target'
        request_url = call_url(method_url)
        data_request = json.load(urlopen(request_url))
        data.append(data_request)
    
    # Transform list of dicts to DataFrame
    df = pd.DataFrame(data)
    
    return df

# Test the code    
symbol_list = ['aapl','tsla']

df = price_target_call(symbol_list)
print(df)