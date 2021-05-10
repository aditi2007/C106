import pandas as pd
import plotly.express as px
import math
import csv
with open(r"C:\Users\a2z\Downloads\Data-visualization-master\Data-visualization-master\csv files\cups of coffee vs hours of sleep.csv")as c:
    df=csv.DictReader(c)
    fig=px.bar(df,x="sleep in hours", y="Coffee in ml", color="week")
    fig.show()