from pandas_datareader import data, wb
import datetime

def get_stock_prices():
    data_source = "morningstar"
    now = datetime.datetime.now()
    start = datetime.datetime(now.year, now.month, now.day-1)
    end = datetime.datetime(now.year, now.month, now.day-1)
    BAC = data.DataReader("BAC", data_source, start, end)
    return("Bank of America (BAC) >>> Opening {} -- Closing {} USD".format(BAC.iloc[0,3], BAC.iloc[0,0]))
    