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

def tops_pull():
    """Returns real time Top of Book Quote and Last Sale Feed (TOPS) data.
    IEX TOPS documentation: https://iextrading.com/trading/market-data/#tops
    
    Returns:
    - df: high, low, and average price targets for list of tickers; tpye = Pandas DataFrame
    
    Response Attributes:
        KEY	DESCRIPTION
        symbol:         refers to the stock ticker.
        bidSize:        refers to amount of shares on the bid on IEX.
        bidPrice:       refers to the best bid price on IEX.
        askSize:        refers to amount of shares on the ask on IEX.
        askPrice:       refers to the best ask price on IEX.
        volume:         refers to shares traded in the stock on IEX.
        lastSalePrice:  refers to last sale price of the stock on IEX.
        lastSaleSize:   refers to last sale size of the stock on IEX.
        lastSaleTime:   refers to last sale time in epoch time of the stock on IEX.
        lastUpdated:    refers to the last update time of the data in milliseconds.
        sector:         refers to the sector the security belongs to.
        securityType:   refers to the common issue type.
    """
    method_url = '/tops'
    request_url = call_url(method_url)
    data_request = json.load(urlopen(request_url))
    
    # Transform list of dicts to DataFrame
    df = pd.DataFrame(data_request)
    
    return df
    
all_tops_df = tops_pull()
#print(all_tops_df[all_tops_df['symbol'] == 'QQQ'])

# Common stock filter
all_stocks_df = all_tops_df[all_tops_df['securityType'].isin(['cs','et'])]
print(all_stocks_df.head(50))
print(len(all_stocks_df))

# Price filter


# Volumne fliter