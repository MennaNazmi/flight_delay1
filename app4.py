from flask import Flask ,render_template
import plotly.graph_objects as go
from flask_mysqldb import MySQL 
import mysql.connector
import streamlit as st
import csv 
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import datetime
import altair as alt

#csv_data=csv.reader(open('fli_data/fli.csv'))
df = pd.read_csv("fli_data/fli.csv") 
#print(df)
#print(df.columns)
#st.title("HOLA ")
df['dep_sch_time']=df['dep_sch_time'].str[0:5]
df['dep_act_time']=df['dep_act_time'].str[0:5]
df['arr_sch_time']=df['arr_sch_time'].str[0:5]
df['arr_act_time']=df['arr_act_time'].str[0:5]



df_time=df[['dep_sch_time','dep_act_time','arr_sch_time','arr_act_time','flight_name2']]
#all_df=df[df['Order Date'].str[0:2]!='Or']

#df_time['dep_sch_time'] = pd.to_datetime(df_time['dep_sch_time'],errors='coerce').dt.time

#df_time['dep_act_time'] = pd.to_datetime(df_time['dep_act_time'],errors='coerce').dt.time
#df_time['arr_sch_time'] = pd.to_datetime(df_time['arr_sch_time'],errors='coerce').dt.time
#df_time['arr_act_time'] = pd.to_datetime(df_time['arr_act_time'],errors='coerce').dt.time


df_time=df_time.dropna()

#df2 = pd.to_datetime(df_time['dep_sch_time']).dt.time

#print(df_time['dep_sch_time'])
#print(df_time)
#print(df_time['dep_act_time'].loc[8])
#plt.bar (df_time['dep_sch_time'],df_time['flight_name2'])
#plt.show()

#df_time.drop(df_time.index[[1,8]])
df_time_clean=df_time.drop(df_time.index[[1,8]])

st.title("HOLA")


df_dep = pd.DataFrame(
    {
        'dep_sch_time': df_time_clean['dep_sch_time'],
        'dep_act_time': df_time_clean['dep_act_time'],
        #,'flight_name2': df_time_clean['flight_name2']
    },
    columns=['dep_sch_time', 'dep_act_time']#, 'flight_name2']
)

st.write(df_dep)
#df_time_clean['dep_sch_time'].time() - df_time_clean['dep_act_time'].time()
#print(df_time_clean['dep_sch_time'] - df_time_clean['dep_act_time'])

st.line_chart(df_dep)

