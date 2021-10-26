import csv
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('data.csv')

student_df = df.loc[df['student_id']=='TRL_987']

print(student_df.groupby('level')['attempt'].mean())

fig = go.Figure(go.Scatter(
        x=student_df.groupby('level')['attempt'].mean(),
        y = ['level 1','level','level 3','level 4'],
        orientation = 'h'))

    fig.show()