'''this file takes in an asset (ex. the array from the data scraping tool), and a timespan (integer value representing days) 
and returns the plotted moving average of the asset, for the given timespan'''
import matplotlib.pyplot as plt
def plotMA_Close(asset, timespan):
  asset['Open'].plot(figsize=(16,8))
  asset['MA'] = asset['Open'].rolling(timespan).mean()
  asset['MA'].plot(label=f'MA{timespan}')
  plt.show()
