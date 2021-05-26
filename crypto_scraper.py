'''The general idea of this file is to build a web scraper for cryptocurrency trading information.
I would like to modify this so that it is subject to user input and ideally using a GUI to solicit input, and return the desired information. 
My idea is that users will be able to select cryptocurrency tickers from a dictionary to add to their own personal list.
That list would be saved for the user and the accessible at any time.
Honestly, I think it would be nice first step just to send a notification like "Your [buy/sell] conditions for [asset] are currently met!" to user.
Obviously, my skills and this project are still in infancy [at least as of 5/26/2021] feel free to share input!'''


# imports for data analysis
from datetime import datetime as dt
import numpy
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# list of crypto tickers. I would like to 
cryptos = ['BTC-USD', 'ETH-USD', 'ADA-USD', 'DOGE-USD']

today = dt.now().date()
one_yr = today.replace(year=today.year - 1)
three_yr = today.replace(year=today.year - 3)
five_yr = today.replace(year=today.year - 5)
print(f'Today: {today} \n -1yr: {one_yr} \n -3yr: {three_yr} \n -5yr: {five_yr}')


crypto_datasets = {

}
# use datareader to scrape for crypto data
def scrape(start, end):
    for coin in cryptos:
        dataSet = web.DataReader(coin, 'yahoo', start, end)
        crypto_datasets.update({coin:dataSet})

scrape(one_yr, today)
scrape(three_yr, today)
scrape(five_yr, today)
