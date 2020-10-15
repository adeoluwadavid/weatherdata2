# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:44:48 2020
@author: Adewole
"""
import pandas as pd
import matplotlib.pyplot as plt
#Read excel file
df1 = pd.read_excel('Keffi_Weather.xlsx',sheet_name=None)

#Concat the files into a single file
df = pd.concat(df1.values(),ignore_index=True)

#export it into excel
df.to_excel(r'C:\Users\Adewole\Documents\Astra_Agric\Keffi_Weather2\Kfweather2.xlsx', index = False, header=True)

