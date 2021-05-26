
import matplotlib.pyplot as plt

def EWMA(asset, timespan):
  asset[f'{timespan} EWMA'] = asset['Close'].ewm(span=timespan).mean()
  asset.plot()
  plt.show()
