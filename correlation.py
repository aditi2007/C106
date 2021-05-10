import pandas as pd
import plotly.express as px
import math
import csv
with open(r"C:\Users\a2z\Downloads\Data-visualization-master\Data-visualization-master\csv files\Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv")as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Ice-cream Sales", y="Temperature")
    fig.show()

