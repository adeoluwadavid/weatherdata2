# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 09:00:51 2020

@author: Adewole
"""
#periods=len(df)
#end='12/31/2016'
import pandas as pd

#Read excel file
df = pd.read_excel('Keffi_Weather_Combined.xlsx',)
#print(df)
p = pd.date_range(start='1/1/2014',periods=len(df),freq='1H' )
df.set_index(p,inplace=True)
print(df)
#
#Concat the files into a single file
#df1 = pd.concat(df.values(),ignore_index=True)
#
##export it into excel
#df1.to_excel(r'C:\Users\Adewole\Documents\Astra_Agric\Keffi_Weather2\David\2018_C.xlsx', index = False, header=True)