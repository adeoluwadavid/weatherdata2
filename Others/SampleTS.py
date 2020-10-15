# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 08:29:20 2020

@author: Adewole
"""

import pandas as pd

#df = pd.read_excel('Keffi_Weather_Combined.xlsx')

df = pd.read_excel('Sample.xlsx')
print(df)
p = pd.date_range(start='2/1/2014',periods=len(df), freq='D' )
df.set_index(p,inplace=True)
print(df)

#df.to_excel('C:\Users\Adewole\Documents\Astra_Agric\Keffi_Weather2\Sample2.xlsx',index=False)
