import dash, plotly.express as px, pandas as pd, numpy as np
#https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Other/juplab3/simple_app.ipynb

df = px.data.gapminder()
dfindia=df.loc[df.country.isin(['India'])]
fig = px.line(data_frame=dfindia, x='year', y='gdpPercap',color='country')
fig.show
