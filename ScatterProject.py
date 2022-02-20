import pandas as pd
import plotly.express as px

df = pd.read_csv("cases.csv")
fig = px.scatter(df,x="cases",y="date",color ="country", size_max=30)

fig.show()