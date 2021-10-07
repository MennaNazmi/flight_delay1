#graph  get data mysql 
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest 

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

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="vegatry1",
    database="flaskapp"
)


mycursor=mydb.cursor(buffered=True) 


number_flights=[]
each_airport=[]

def run_query(query):
    with mydb.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("""
Select airport_city,count(airport_fs) as count_fli 
from flight_t2 group by airport_city order by count_fli""")
for row in rows:
    print(row)
    number_flights.append(row[1])
    each_airport.append(row[0])

flights_each_airport=pd.DataFrame({
    'number_of_flights': number_flights,
    'airport': each_airport
    })

fig=px.bar(flights_each_airport,x="number_of_flights", y="airport",orientation='h',title='Number of Flights Each Airport')
st.plotly_chart(fig)


##############################AVG DELAY PER AIRPORT #############################

rows=run_query("""select arr_airport_name , avg(delay_dep) as avg_delay_dep,avg(delay_arr) as avg_delay_arr  # #,AVG() as avg_arr_delay
from flight_t2
group by arr_airport_name
order by avg_delay_arr desc
limit 6""")

dep_airport_to_li=[]
avg_dep_delay_li=[]
avg_arr_delay_li=[]
# Print results.
for row in rows:
    dep_airport_to_li.append(row[0])
    avg_dep_delay_li.append(row[1])
    avg_arr_delay_li.append(row[2])
    


df_avg_dep_arr=pd.DataFrame({
    'dep_airport_to_li': dep_airport_to_li,
    'avg_dep_delay_li':avg_dep_delay_li,
    'avg_arr_delay_li':avg_arr_delay_li
})

fig_avg_dep_arr_airport= go.Figure(data=[
    go.Bar(name='avg dep delay', x=dep_airport_to_li, y=avg_dep_delay_li),
    go.Bar(name='avg arr delay', x=dep_airport_to_li, y=avg_arr_delay_li)])

fig_avg_dep_arr_airport.update_layout(barmode='group',title="Average Delay Per Airport",xaxis_title="Airport",yaxis_title="Average Delay")
st.plotly_chart(fig_avg_dep_arr_airport)

####################Delay per airline###########################

rows=run_query("""select carrier_name as airline, avg(delay_dep) as avg_delay_dep,avg(delay_arr) as avg_delay_arr  # #,AVG() as avg_arr_delay
from flight_t2
group by airline
order by avg_delay_arr desc
limit 6""")

airline_to_li=[]
avg_dep_delay_li=[]
avg_arr_delay_li=[]
# Print results.
for row in rows:
    airline_to_li.append(row[0])
    avg_dep_delay_li.append(row[1])
    avg_arr_delay_li.append(row[2])
    


df_avg_dep_arr=pd.DataFrame({
    'airline_to_li': airline_to_li,
    'avg_dep_delay_li':avg_dep_delay_li,
    'avg_arr_delay_li':avg_arr_delay_li
})

fig_avg_dep_arr_airline= go.Figure(data=[
    go.Bar(name='avg dep delay', x=airline_to_li, y=avg_dep_delay_li),
    go.Bar(name='avg arr delay', x=airline_to_li, y=avg_arr_delay_li)])

fig_avg_dep_arr_airline.update_layout(barmode='group',title="Average Delay Per Airline",xaxis_title="Airline",yaxis_title="Average Delay")
st.plotly_chart(fig_avg_dep_arr_airline)
#######################avg delay per flight type###############################

rows=run_query("""select flight_type , avg(delay_dep) as avg_delay_dep,avg(delay_arr) as avg_delay_arr  # #,AVG() as avg_arr_delay
from flight_t2
group by flight_type
order by avg_delay_arr desc
limit 6""")

flight_type_li=[]
avg_dep_delay_li=[]
avg_arr_delay_li=[]
# Print results.
for row in rows:
    flight_type_li.append(row[0])
    avg_dep_delay_li.append(row[1])
    avg_arr_delay_li.append(row[2])
    


df_avg_dep_arr=pd.DataFrame({
    'flight_type_li': flight_type_li,
    'avg_dep_delay_li':avg_dep_delay_li,
    'avg_arr_delay_li':avg_arr_delay_li
})

fig_avg_dep_arr_flight_type= go.Figure(data=[
    go.Bar(name='avg dep delay', x=flight_type_li, y=avg_dep_delay_li),
    go.Bar(name='avg arr delay', x=flight_type_li, y=avg_arr_delay_li)])

fig_avg_dep_arr_flight_type.update_layout(barmode='group',title="Average Delay Per Flight Type",xaxis_title="Flight Type",yaxis_title="Average Delay")
st.plotly_chart(fig_avg_dep_arr_flight_type)
###################################

f_type_seats = {"Boeing 737-800":162,
"Airbus A321neo":244,
"Boeing 777-300ER":396,
"Airbus A330-300":440,
"Airbus A350-900":162,
"Airbus A220-300":440,
"Airbus A320":170,
"Boeing 737-700":143,
"Boeing 787-9":296,
"Airbus A320neo":194,
"Boeing 787-8":248
}