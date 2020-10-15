# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:04:49 2020

@author: Adewole
"""

import pandas as pd

#df = pd.read_excel('Keffi_Weather_Combined.xlsx')

df = pd.read_excel('2014.xlsx', 'Feb')

print(df)
p = pd.date_range(start='2/1/2014',periods=len(df), freq='H' )
df.set_index(p,inplace=True)
print(df)

#df.to_excel('C:\Users\Adewole\Documents\Astra_Agric\Keffi_Weather2\Sample2.xlsx',index=False)
