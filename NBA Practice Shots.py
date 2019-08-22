# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:33:06 2019

@author: jakes
"""

import requests as r
import json
 
# Chrome's user-agent string, to simulate a browser visiting the webpage
headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

# Stephen Curry's player id
player_id = 201939

# DeMarcus Cousins' player id
cousins_id = 202326

# Bradley Beal's player id
beal_id = 203078
# season details
season = '2018-19'
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
 'PlayerID': beal_id,
 'PlayerPosition': '',
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
res.raise_for_status()
import pandas as pd


res_json = res.json()
 
# column names
rows = res_json['resultSets'][0]['headers']
# row content
shots_data = res_json['resultSets'][0]['rowSet']

shots_df = pd.DataFrame(shots_data, columns=rows)

shots_df['EVENT_TYPE'].unique()

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
fig.write_html('first_figure.html', auto_open=True)


# list containing all the shapes
court_shapes = []
 
outer_lines_shape = dict(
  type='rect',
  xref='x',
  yref='y',
  x0='-250',
  y0='-47.5',
  x1='250',
  y1='422.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)
 
court_shapes.append(outer_lines_shape)

hoop_shape = dict(
  type='circle',
  xref='x',
  yref='y',
  x0='7.5',
  y0='7.5',
  x1='-7.5',
  y1='-7.5',
  line=dict(
    color='rgba(10, 10, 10, 1)',
    width=1
  )
)
 
court_shapes.append(hoop_shape)

backboard_shape = dict(
  type='rect',
  xref='x',
  yref='y',
  x0='-30',
  y0='-7.5',
  x1='30',
  y1='-6.5',
  line=dict(
    color='rgba(10, 10, 10, 1)',
    width=1
  ),
  fillcolor='rgba(10, 10, 10, 1)'
)
 
court_shapes.append(backboard_shape)

outer_three_sec_shape = dict(
  type='rect',
  xref='x',
  yref='y',
  x0='-80',
  y0='-47.5',
  x1='80',
  y1='143.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)
 
court_shapes.append(outer_three_sec_shape)

inner_three_sec_shape = dict(
  type='rect',
  xref='x',
  yref='y',
  x0='-60',
  y0='-47.5',
  x1='60',
  y1='143.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)
 
court_shapes.append(inner_three_sec_shape)

left_line_shape = dict(
  type='line',
  xref='x',
  yref='y',
  x0='-220',
  y0='-47.5',
  x1='-220',
  y1='92.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)
 
court_shapes.append(left_line_shape)

right_line_shape = dict(
  type='line',
  xref='x',
  yref='y',
  x0='220',
  y0='-47.5',
  x1='220',
  y1='92.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)
 
court_shapes.append(right_line_shape)

three_point_arc_shape = dict(
  type='path',
  xref='x',
  yref='y',
  path='M -220 92.5 C -70 300, 70 300, 220 92.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)
 
court_shapes.append(three_point_arc_shape)

center_circle_shape = dict(
  type='circle',
  xref='x',
  yref='y',
  x0='60',
  y0='482.5',
  x1='-60',
  y1='362.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)
 
court_shapes.append(center_circle_shape)

res_circle_shape = dict(
  type='circle',
  xref='x',
  yref='y',
  x0='20',
  y0='442.5',
  x1='-20',
  y1='402.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)
 
court_shapes.append(res_circle_shape)

free_throw_circle_shape = dict(
  type='circle',
  xref='x',
  yref='y',
  x0='60',
  y0='200',
  x1='-60',
  y1='80',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)
 
court_shapes.append(free_throw_circle_shape)

res_area_shape = dict(
  type='circle',
  xref='x',
  yref='y',
  x0='40',
  y0='40',
  x1='-40',
  y1='-40',
  line=dict(
    color='rgba(10, 10, 10, 1)',
    width=1,
    dash='dot'
  )
)
 
court_shapes.append(res_area_shape)



missed_shot_trace = go.Scatter(
    x = shots_df[shots_df['EVENT_TYPE'] == 'Missed Shot']['LOC_X'],
    y = shots_df[shots_df['EVENT_TYPE'] == 'Missed Shot']['LOC_Y'],
    mode = 'markers',
    name = 'Missed Shot',
    marker = dict(
        size = 5,
        color = 'rgba(255, 255, 0, .8)',
        line = dict(
            width = 1,
            color = 'rgb(0, 0, 0, 1)'
        )
    )
)
 
made_shot_trace = go.Scatter(
    x = shots_df[shots_df['EVENT_TYPE'] == 'Made Shot']['LOC_X'],
    y = shots_df[shots_df['EVENT_TYPE'] == 'Made Shot']['LOC_Y'],
    mode = 'markers',
    name = 'Made Shot',
    marker = dict(
        size = 5,
        color = 'rgba(0, 200, 100, .8)',
        line = dict(
            width = 1,
            color = 'rgb(0, 0, 0, 1)'
        )
    )
)
 
data = [missed_shot_trace, made_shot_trace]
 
layout = go.Layout(
    title='Shots by Bradley Beal in NBA Season 2018-19',
    showlegend=True,
    xaxis=dict(
        showgrid=False,
        range=[-300, 300]
    ),
    yaxis=dict(
        showgrid=False,
        range=[-100, 500]
    ),
    height=600,
    width=650,
    shapes=court_shapes
)
 
fig = go.Figure(data=data, layout=layout)
iplot(fig)
fig.write_html('second_figure.html', auto_open=True)







