import csv
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('data.csv')

print(df.groupby('level')['attempt'].mean())

fig = go.Figure(go.Scatter(
        x=df.groupby('level')['attempt'].mean(),
        y=['level 1','level 2','level3 ','level 4'],
        orientation = 'h'))

    fig.show()