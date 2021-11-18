# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 19:03:40 2021

@author: awi027
"""

import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as shc

data = pd.read_csv(os.path.join(os.getcwd(), 'data', 'd02_prepared_data', 'prepared_data.csv'))

# Attacking and defensive stats

input_data = data.drop(['Team'], axis = 1)

scaler = StandardScaler()
scaler.fit(input_data)
input_data_scaled = scaler.transform(input_data)

plt.figure()
plt.title("Dendrograms")
dendrogram = shc.dendrogram(shc.linkage(input_data_scaled, method='ward'))

# Try correlation plot

plot_corr(input_data_scaled)

# Attacking stats

input_attacking_data = data[['OutOfBox', 'NearShots', 'OpenPlay', 'Counter', 'SetPiece', 'PenaltiesTaken', 
                             'DribblesTotal', 'LongBallsAttempted', 'ShortPassesAttempted', 'CrossesAttempted',
                             'WingPlay']]

scaler = StandardScaler()
scaler.fit(input_attacking_data)
input_attacking_data_scaled = scaler.transform(input_attacking_data)

plt.figure()
plt.title("Dendrograms")
dendrogram = shc.dendrogram(shc.linkage(input_attacking_data_scaled, method='ward'))