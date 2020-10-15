# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 17:05:46 2020

@author: Adewole
"""

import pandas as pd

p = pd.date_range(start='1/1/2014', end='1/09/2014', freq='1H')
print(p)
p.to_csv('C:\Users\Adewole\Documents\Astra_Agric\Keffi_Weather2\ts.xlsx', index=False)