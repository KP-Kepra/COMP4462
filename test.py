import pandas as pd 
import numpy as np
import json
import os

for i in range(1, 13):
  print(i)
  df = pd.read_csv('200_2018_{:02d}.csv'.format(i))
  df['month'] = i

  while 'index' in df.columns:
    del df['index'] 

  while 'Unnamed: 0' in df.columns:
    del df['Unnamed: 0']

  df = df[['subreddit', 'length', 'score', 'month']]

  ow_data = df[df.subreddit == 'Overwatch'].head(50)
  lol_data = df[df.subreddit == 'leagueoflegends'].head(50)
  pubg_data = df[df.subreddit == 'PUBATTLEGROUNDS'].head(50)
  csgo_data = df[df.subreddit == 'GlobalOffensive'].head(50)
  smash_data = df[df.subreddit == 'smashbros'].head(50)
  hs_data = df[df.subreddit == 'hearthstone'].head(50)
  dota_data = df[df.subreddit == 'DotA2'].head(50)
  gta_data = df[df.subreddit == 'GrandTheftAutoV'].head(50)
  tf_data = df[df.subreddit == 'tf2'].head(50)

  print(df[df.subreddit == 'Overwatch'].shape)
  print(df[df.subreddit == 'leagueoflegends'].shape)
  print(df[df.subreddit == 'PUBATTLEGROUNDS'].shape)
  print(df[df.subreddit == 'GlobalOffensive'].shape)
  print(df[df.subreddit == 'smashbros'].shape)
  print(df[df.subreddit == 'hearthstone'].shape)
  print(df[df.subreddit == 'DotA2'].shape)
  print(df[df.subreddit == 'GrandTheftAutoV'].shape)
  print(df[df.subreddit == 'tf2'].shape)

  new_data = pd.concat([ow_data, lol_data, pubg_data, csgo_data, smash_data, hs_data, dota_data, gta_data, tf_data])

  df.to_csv('50_2018_{:02d}.csv'.format(i), index=False)
