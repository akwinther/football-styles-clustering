# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 16:20:06 2021

@author: awi027
"""

import pandas as pd
import os
import glob

# Load files and concat into one dataframe

PATH = os.path.join(os.getcwd(), "data", "scraped_data")

all_files = glob.glob(PATH + "/*.csv")

file_list = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    file_list.append(df)

whoscored_data = pd.concat(file_list, axis=0, ignore_index=True)

# Make new columns
whoscored_data['NearShots'] = whoscored_data['SixYardBox'] + whoscored_data['PenaltyArea']
whoscored_data['LongBallsAttempted'] = whoscored_data['LongBallAccurate'] + whoscored_data['LongBallInaccurate']
whoscored_data['ShortPassesAttempted'] = whoscored_data['ShortPassAccurate'] + whoscored_data['ShortPassInaccurate']
whoscored_data['CrossesAttempted'] = whoscored_data['CrossAccurate'] + whoscored_data['CrossInaccurate']
whoscored_data['WingPlay'] = whoscored_data['LeftSide'] + whoscored_data['RightSide']

processed_data = whoscored_data[['Team', 'OutOfBox', 'NearShots', 'OpenPlay', 'Counter', 'SetPiece', 'PenaltiesTaken', 
                                'DribblesTotal', 'LongBallsAttempted', 'ShortPassesAttempted', 'CrossesAttempted', 
                                'WingPlay', 'TacklesAttempted', 'FoulsCommitted', 'Interceptions',
                                'TotalClearances', 'ShotsBlocked', 'CrossesBlocked', 'PassesBlocked']]

processed_data.to_csv(os.path.join(os.getcwd(), 'data', 'processed_data', 'processed_data.csv'), index = False)
