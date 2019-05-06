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

  print(df[df.subreddit == 'Overwatch'].shape)
  print(df[df.subreddit == 'leagueoflegends'].shape)
  print(df[df.subreddit == 'PUBATTLEGROUNDS'].shape)
  print(df[df.subreddit == 'GlobalOffensive'].shape)
  print(df[df.subreddit == 'smashbros'].shape)
  print(df[df.subreddit == 'hearthstone'].shape)
  print(df[df.subreddit == 'DotA2'].shape)
  print(df[df.subreddit == 'GrandTheftAutoV'].shape)
  print(df[df.subreddit == 'tf2'].shape)

  df.to_csv('200_2018_{:02d}.csv'.format(i), index=False)
