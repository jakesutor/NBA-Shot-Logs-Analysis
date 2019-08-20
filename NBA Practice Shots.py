# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:33:06 2019

@author: jakes
"""

import requests as r
 
# Chrome's user-agent string, to simulate a browser visiting the webpage
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}
 
# Stephen Curry's player id
player_id = 201939
 
# season details
season = '2015-16'
season_type = 'Regular Season'
 
# request parameters
req_params = {
 'AheadBehind': '',
 'ClutchTime': '',
 'ContextFilter': '',
 'ContextMeasure': 'FGA',
 'DateFrom': '',
 'DateTo': '',
 'EndPeriod': '',
 'EndRange': '',
 'GameID': '',
 'GameSegment': '',
 'LastNGames': 0,
 'LeagueID': '00',
 'Location': '',
 'Month': 0,
 'OpponentTeamID': 0,
 'Outcome': '',
 'Period': 0,
 'PlayerID': player_id,
 'PointDiff': '',
 'Position': '',
 'RangeType': '',
 'RookieYear': '',
 'Season': season,
 'SeasonSegment': '',
 'SeasonType': season_type,
 'StartPeriod': '',
 'StartRange': '',
 'TeamID': 0,
 'VsConference': '',
 'VsDivision': ''
}
 
res = r.get('http://stats.nba.com/stats/shotchartdetail', params=req_params, headers=headers)
import pandas as pd
 
res_json = res.json()
 
# column names
rows = res_json['resultSets'][0]['headers']
# row content
shots_data = res_json['resultSets'][0]['rowSet']
 
shots_df = pd.DataFrame(shots_data, columns=rows)

shots_df['EVENT_TYPE'].unique()
array([u'Made Shot', u'Missed Shot'], dtype=object)

import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode()
 
shot_trace = go.Scatter(
    x = shots_df[shots_df['EVENT_TYPE'] == 'Missed Shot']['LOC_X'],
    y = shots_df[shots_df['EVENT_TYPE'] == 'Missed Shot']['LOC_Y'],
    mode = 'markers'
)
 
data = [shot_trace]
layout = go.Layout(
    showlegend=False,
    height=600,
    width=600
)
 
fig = go.Figure(data=data, layout=layout)
iplot(fig)


shots_df[shots_df['EVENT_TYPE'] == 'Made Shot']










