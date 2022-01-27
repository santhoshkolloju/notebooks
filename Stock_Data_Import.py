# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 12:08:03 2021

@author: Harshal Acharya
"""

import numpy as np
import pandas as pd
import yfinance as yf
import os

#Making List of All Nifty 500 Stock from CSV File
os.chdir("D:\R&D Work")
Nifty500_Stock = pd.read_csv("Nifty_500.csv")

#Making List From Datafarme Column
Stock_List = Nifty500_Stock["Stock_List"].tolist()

#Making an empty frame
main_df = pd.DataFrame()

#For each stock we are sacing data in df and merging it with main data frame
for i in range(0,len(Stock_List)):
    df = yf.download(Stock_List[i], interval = "1mo")
    df = df.dropna()
    a = []
    b = len(df)
    c = []
    for j in range(0,b):
        a.append(Stock_List[i])
        c.append(j)
    df.insert(6,"name",a)
    df.insert(7,"Check",c)
    main_df = pd.concat([main_df,df])

#exporting csv file
main_df.to_csv(r"D:\R&D Work\4.0) Finance\4.4) Trading\Momentum_Investment_Stretegy\Nifty500")

#importing csv file with 1 year change data
price_df = pd.read_csv("D:\R&D Work\All_Price.csv")

#List of All Months from jan-2010 to dec-2020
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
years = ["10","11","12","13","14","15","16","17","18","19","20"]
month_list = []
for year in years:
    for month in months:
        month_list.append(month + "-" + year)
         
#Creating Top40 Stocks for each month.
top_40 = pd.DataFrame()

for month in month_list:
    temp_df = price_df[price_df["date"] == month]
    temp_df.sort_values(by = ["1_year_change"], inplace = True, ascending = False)
    temp_df = temp_df.iloc[:40]
    top_40 = pd.concat([top_40,temp_df])

top_40.to_csv(r"D:\R&D Work\4.0) Finance\4.4) Trading\Momentum_Investment_Stretegy\Top_40.csv")

 
        
    
