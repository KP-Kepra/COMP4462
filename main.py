import pandas as pd 
import numpy as np
import json
import os

for i in range(1, 13):
  raw_data = pd.read_csv("new_2018_{:02d}.csv".format(i))

  old_csv_path = '200_2018_{:02d}.csv'.format(i)

  if os.path.isfile(old_csv_path): old_200_csv = pd.read_csv(old_csv_path)
  else: old_200_csv = None

  # raw_smash_data = raw_data[raw_data.subreddit == 'smashbros'].head(200)
  # raw_hearthstone = raw_data[raw_data.subreddit == 'hearthstone'].head(200)
  raw_ow_data = raw_data[raw_data.subreddit == 'Overwatch'].head(200)
  raw_lol_data = raw_data[raw_data.subreddit == 'leagueoflegends'].head(200)
  raw_pubg_data = raw_data[raw_data.subreddit == 'PUBATTLEGROUNDS'].head(200)
  raw_csgo_data = raw_data[raw_data.subreddit == 'GlobalOffensive'].head(200)

  raw_data = pd.concat([raw_ow_data, raw_lol_data, raw_pubg_data, raw_csgo_data])
  # raw_data = pd.concat([raw_smash_data, raw_hearthstone])
  if old_200_csv is not None:
    raw_data = pd.concat([old_200_csv, raw_data])

  raw_data = raw_data.reset_index()
  
  while 'index' in raw_data.columns:
    del raw_data['index'] 

  while 'Unnamed: 0' in raw_data.columns:
    del raw_data['Unnamed: 0']

  raw_data.to_csv('200_2018_{:02d}.csv'.format(i))