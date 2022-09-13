# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import pandas as pd
from operator import indexOf
import numpy as np
from turtle import width
import plotly.graph_objects as go

app = Dash(__name__)

df = pd.read_excel("bmwConfig.xlsx",sheet_name='Slip Target', header=None)

#Pull Off First Colomn for Speed
targetSpeed = df[0]
targetSpeed = targetSpeed.drop(index=df.index[0])

#Pull Off First Row for Lean
targetLean = df.iloc[0]
targetLean = targetLean.drop(index=df.index[0])

#Create 2D Array of Slip Target Values
for x in range(1, len(targetLean)+1):
    yArray=[]
    for y in range(1,len(targetSpeed)+1):
        yArray.append(df.iloc[x,y])
        if len(yArray) == 10:
            if x == 1:
                targetSlip = np.array([yArray])
            else:
                targetSlip = np.append(targetSlip,[yArray], axis=0)


#Read Log file
log = pd.read_csv("log1.csv")

#Remove second row that has value types and convert whole dataframe to number
log.drop(log.index[0], inplace=True)
log = log.apply(pd.to_numeric)

#Remove Negative Slip (braking)
brakingValues = log[log['slip']<0].index
log.drop(brakingValues, inplace=True)

#Convert All Lean Angles to positive
log['phi_lean'] = log['phi_lean'].abs()

speed = log['v_front']
slip = log['slip']
lean = log['phi_lean']

#Create Mesh Grid from Target Values
targetLean, targetSpeed = np.meshgrid(targetLean, targetSpeed)

#Real Values Read from Log File
actualLean=lean
actualSpeed=speed
actualSlip=slip

fig = go.Figure(data=[
    go.Surface(x=targetLean, y=targetSpeed, z=targetSlip, opacity=0.5, colorscale='rdbu', name='Target Slip'),
    go.Scatter3d(x=actualLean, y=actualSpeed, z=actualSlip,
    name='Actual Slip Turn 4',
    mode='lines',
   # Only needed if I want dots instead of lines
    #marker=dict(
    #    size=4,
    #    color=z,
    #    colorscale='Viridis',
    #),
    line=dict(
        color='green',
        width=8
    )
    )
    ])
fig.update_layout(title='Target Slip vs Actual Slip - Turn 5 Redbull Ring', autosize=False,
                  width=1000, height=1000,
                  margin=dict(l=65, r=50, b=65, t=90))

fig.update_layout(scene = dict(
                    xaxis_title='Lean Angle (degrees)',
                    yaxis_title='Speed (km/h)',
                    zaxis_title='Slip (%)'))

app.layout = html.Div(children=[
    html.H1(children='BMW M1000RR Analytics Toolkit'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)