import argparse
import serial
import datetime
import time
import os

import csv
import string
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('logdata.csv')
df.dropna(axis=0, how='all',inplace=True)
df.to_csv('output1.csv', index=False)

# read contents of csv file 
file = pd.read_csv("output1.csv") 
##print("\nOriginal file:")
##print(file) 
  
# adding header 
headerList = ['Time(us)','AX(g)', 'AY(g)', 'AZ(g)']

# converting data frame to csv 
file.to_csv("output2.csv", header=headerList, index=False) 
  
data = pd.read_csv("output2.csv")
#print(data.head())

fig = px.line(data, x="Time(us)",y=["AX(g)", "AY(g)", "AZ(g)"],title="Acceleration Data Over Time")
#fig = px.line(data, x="Pkt",y=["AX"],title="ACC data over time")
        
fig.show()
