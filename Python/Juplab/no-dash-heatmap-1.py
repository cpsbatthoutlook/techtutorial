import dash, plotly.express as px, pandas as pd, numpy as np
#https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Plotly_Graphs/Heatmaps/heatmap.py
f = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Plotly_Graphs/Heatmaps/Berlin_crimes.csv")
df = f.groupby(['District'])[
    ['Graffiti','Robbery', 'Agg_assault', 'Burglary']].median().reset_index()
print(df[:15])
df = pd.melt(df, id_vars=['District'], value_vars=['Graffiti', 'Robbery', 'Agg_assault', 'Burglary'],
             var_name='Crime')
print(df[:15])
df = df.pivot('Crime','District','value')
print(df)

fig = px.imshow(df,color_continuous_scale=px.colors.sequential.Plasma,
                title="Berlin Crime Distribution")
fig.update_traces(hoverongaps=False,
                  hovertemplate="District: %{y}"
                                "<br>Crime: %{x}"
                                "<br>Cases: %{z}<extra></extra>"
                  )
fig.update_layout(title_font={'size':27}, title_x=0.5)
fig.show()
