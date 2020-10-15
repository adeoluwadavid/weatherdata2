# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 11:41:20 2020

@author: Adewole
"""

import pandas as pd

day = 5


start = (day - 1) * 24
end = start + 24
#Read excel file
df = pd.read_excel('2018.xlsx', 'Mar')


time = df.iloc[start:end, 0:3]
temperature = df.iloc[start:end, 3:4]


df['Time'] = time
#df['Temperature'] = temperature

print(time)
print()
print(len(time))

#
#print(df)
#p = pd.date_range(start='3/1/2018',periods=len(time),freq='1H' )
#df.set_index(time,inplace=True)
#print(df)