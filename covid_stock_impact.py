# Import the yfinance. If you get module not found error the run !pip install yfinance from your Jupyter notebook
import yfinance as yf
import pdb;pdb.set_trace()
import matplotlib.pyplot as plt
import sys
import os
import pandas as pd

path = os.getcwd()
class CovidStockImpact:
    def __init__(self):
        self.ticker = 'GILD'
        self.path = '../../covid/covid-19-data/public/data/ecdc/new_cases.csv'
        self.stock_data = ''
        self.covid_data = ''
        self.start_date = '2020-06-01'
        self.end_date = '2020-06-26'
        self.country = 'United States'
    def log(self,args):
        print(args)

    def get_stock_data(self):
        # Get the data for the stock AAPL
        stock_information = yf.download(self.ticker,self.start_date,self.end_date)
        self.log(stock_information)
        self.stock_data = stock_information['Close']
    def get_covid_data(self):
        self.covid_data = pd.read_csv(self.path, usecols=['date', self.country]).set_index('date')

    def draw_graph(self):
        pd.merge(self.stock_data, self.covid_data,left_index=True, right_index=True).plot(secondary_y=['United States'])
        plt.title(self.ticker)
        plt.show()

covid_stock_impact = CovidStockImpact()
covid_stock_impact.get_stock_data()
covid_stock_impact.get_covid_data()
covid_stock_impact.draw_graph()
