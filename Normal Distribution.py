import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go

file = pd.read_csv(r"mobile.csv")
avg = file["Avg Rating"]
graph = ff.create_distplot([avg],["Average Rating"],show_hist=False)
graph.show()