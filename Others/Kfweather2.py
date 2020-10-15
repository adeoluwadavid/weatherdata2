# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 08:51:08 2020

@author: Adewole
"""
import pandas as pd
df = pd.read_excel('Keffi_Weather_Combined.xlsx')

#print(df)
p = pd.date_range(start='1/1/2014',periods=len(df), freq='H' )
df.set_index(p,inplace=True)
print(df)