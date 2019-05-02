import pandas as pd 
import numpy as np
import json
import os

for i in range(1, 2):
  raw_data = pd.read_csv("new_2018_0" + str(i) + ".csv")

  raw_ow_data = raw_data[raw_data.subreddit == 'Overwatch'].head(200)
  raw_lol_data = raw_data[raw_data.subreddit == 'leagueoflegends'].head(200)
  raw_pubg_data = raw_data[raw_data.subreddit == 'PUBATTLEGROUNDS'].head(200)
  raw_csgo_data = raw_data[raw_data.subreddit == 'GlobalOffensive'].head(200)

  raw_data = pd.concat([raw_ow_data, raw_lol_data, raw_pubg_data, raw_csgo_data])
  raw_data = raw_data.reset_index()
  del raw_data['index'] 
  del raw_data['Unnamed: 0']
  print(raw_data)
  raw_data.to_csv('200_2018_0' + str(i) + '.csv')