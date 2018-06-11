# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 23:14:33 2018

@author: vtfx3
"""

import json
import pandas as pd
import matplotlib.pyplot as plt


file = 'C:/Users/vtfx3/Desktop/Metis/Daily Data of Commits.txt'

data = pd.read_json(file)

data.columns = ["Day", "Hour", "Num of Commits"]

data['Day'] = data['Day'].replace({0: 'Sun', 1: 'Mon', 2: 'Tues', 3: 'Wed', 4:'Thurs', 5:'Fri',6:'Sat'})

byday = data[["Day","Num of Commits"]]

byday = data.groupby(['Day'])[['Num of Commits']].sum()

MaxByDay = byday.loc[byday['Num of Commits'].idxmax()]

print(MaxByDay)

plt.bar(data["Day"],data["Num of Commits"])

plt.show()