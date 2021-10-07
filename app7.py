##DATA MANIPULATION WITH SQL TO GRAPH
import datetime
from datetime import datetime
from datetime import timedelta
import requests
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import csv
from itertools import zip_longest 
import datetime
import datetime as dt
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

#mycursor.execute()
#myres=mycursor.fetchall()

#df=pd.DataFrame(myres,columns=['flight_code','flight_from','flight_to','airport_from','airport_to','dep_sch','dep_act','arr_sch','arr_act','id'])
#for row in myres:

number_flights=[]
each_airport=[]
def run_query(query):
    with mydb.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("Select airport_to,count(airport_to) from fli_data_table group by flight_to")
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





#####################################################


rows = run_query("select * from fli_data_table  ")


flight_code=[]
flight_date=[]
from_dep=[]
flight_from=[]
flight_to=[]
airport_from=[]
airport_to=[]
dep_sch=[]
dep_act=[]
arr_sch=[]
arr_act=[]
id=[]

# Print results.
for row in rows:
    flight_code.append(row[0])
    flight_date.append(row[1])
    from_dep.append(row[2])
    flight_from.append(row[3])
    flight_to.append(row[4])
    airport_from.append(row[5])
    airport_to.append(row[6])
    dep_sch.append(row[7])
    dep_act.append(row[8])
    arr_sch.append(row[9])
    arr_act.append(row[10])
    id.append(row[11])

   
###create DATAframe of the DATA that we get from MYSQL 
df=pd.DataFrame({
    'flight_code': flight_code,
    'flight_date':flight_date,
    'from_dep':from_dep,
    'flight_from': flight_from,
    'flight_to':flight_to,
    'airport_from':airport_from,
    'airport_to':airport_to,'dep_sch':dep_sch,
    'dep_act':dep_act,'arr_sch':arr_sch,'arr_act':arr_act,'id':id
})

df_for_sider=df['airport_to'].unique()

#choose_airline=st.sidebar.selectbox("select the airline",df_for_sider)

df['dep_sch']=df['dep_sch'].str[0:5]
df['dep_act']=df['dep_act'].str[0:5]
df['arr_sch']=df['arr_sch'].str[0:5]
df['arr_act']=df['arr_act'].str[0:5]
#print(pd.to_datetime(df['arr_sch']))
#df['arr_sch']=pd.to_datetime(df['arr_sch'])
#print(df['arr_act'].str.isalpha())
#print(df['arr_act'].str.isnumeric())
#df['arr_act']=df['arr_act'].str.isalpha()
#print(pd.to_numeric(df['arr_act'][5] ))
#df.drop(df['arr_act']=="-- ")
#df.drdf['arr_act']op(df['arr_act']=="-- ")



df = df[df.arr_act != "-- "] 
df = df[df.dep_act != "-- "]
time_format="%H:%M:%S"
df['dep_sch']=pd.to_datetime(df['dep_sch']).dt.strftime(time_format)
df['dep_act']=pd.to_datetime(df['dep_act']).dt.strftime(time_format)
df['arr_sch']=pd.to_datetime(df['arr_sch']).dt.strftime(time_format)
df['arr_act']=pd.to_datetime(df['arr_act']).dt.strftime(time_format)


#datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

df
#print(df['arr_act']-df['arr_sch'])
df['delay_t']=np.where(df['arr_sch'] > df['arr_act'],"early","late") 

#df['diff_min']=np.where(df['delay_t'] == "early",df['arr_sch'] - df['arr_act'],df['arr_act'] - df['arr_sch']) 

#df['diff_min']=df['arr_sch']-df['arr_act']     
    #df['delay_arr']=df['arr_sch']-df['arr_act']

#print(df[['arr_sch','arr_act','delay_arr']].head())
print(df.head(10))


#rows = run_query("select distinct flight_date from fli_data_table  ")
#dist_days=[]
#for i in rows:
    #dist_days.append(i)
    
st.sidebar.header('Choose the day?')

selected_day=st.sidebar.selectbox('Day',set(flight_date))
st.sidebar.header('Choose the airport?')
selected_airport=st.sidebar.selectbox('airport',set(airport_to))

#hours_de=st.sidebar.slider("delay every ",min_value=0,max_value=12,step=1)
@st.cache  # 👈 Added this
def load_day(sel_arg):
    return sel_arg


res_day = load_day(selected_day)

st.write("Result:", res_day)
df_temp=df[['flight_date','flight_code','airport_to','delay_t']]
#df_temp

number_flights_each_day = df_temp.groupby('flight_date').count()
print(number_flights_each_day)
print("$$")


fli_count_df=pd.DataFrame(
    df_temp['flight_date']
    ,columns=['flight_date']
)


fil1=fli_count_df[fli_count_df['flight_date'].isin([selected_day])]
fli_count_df[df['flight_date'].isin([selected_day])]

df_temp[df['flight_date'].isin([selected_day]) & df['airport_to'].isin([selected_airport])]

#############################

rows = run_query("select SUBSTRING_INDEX(flight_to, ',', -1) as country , count(flight_code) as count_flights from fli_data_table group by country ")

country_li=[]
count_flights_li=[]

# Print results.
for row in rows:
    country_li.append(row[0])
    count_flights_li.append(row[1])



print(country_li,count_flights_li)

df_flight_count=pd.DataFrame({
    'country_li': country_li,
    'count_flights_li':count_flights_li
})



fig_flights_count_each_country = px.bar(df_flight_count, x='country_li', y='count_flights_li')
#fig.show()
st.plotly_chart(fig_flights_count_each_country)


###################delay arrival late early ontime########
rows=run_query(
    """
select time_stat,airport_to,
count(flight_code) as count_flights
from(
select arr_sch,arr_act,flight_code,airport_to,
CASE 
    WHEN arr_sch>arr_act THEN "early"
    WHEN arr_sch<arr_act  THEN "late"
    ELSE "on time"
 END as time_stat
 from fli_data_table
where arr_act != '-- '
)  t1
group by airport_to,time_stat"""
)


fli_stat_li=[]
airport_to_li=[]
count_fli_stat_li=[]

# Print results.
for row in rows:
    fli_stat_li.append(row[0])
    airport_to_li.append(row[1])
    count_fli_stat_li.append(row[2])


df_flight_stat_count=pd.DataFrame({
    'fli_stat_li': fli_stat_li,
    'airport_to_li':airport_to_li,
    'count_fli_stat_li':count_fli_stat_li
})



fig_flights_stat_count = px.bar(df_flight_stat_count, x='airport_to_li', y='count_fli_stat_li',color='fli_stat_li', title="Delay in Arrival")
#fig.show()
st.plotly_chart(fig_flights_stat_count)

##############################dep_time late early ontime######


rows=run_query(
    """select time_stat,airport_to,
count(flight_code) as count_flights
from(
select arr_sch,arr_act,flight_code,airport_to,
CASE 
    WHEN dep_sch>dep_act THEN "early"
    WHEN dep_sch<dep_act  THEN "late"
    ELSE "on time"
 END as time_stat
 from fli_data_table
where arr_act != '-- '
)  t1
group by airport_to,time_stat"""


)


dep_fli_stat_li=[]
dep_airport_to_li=[]
dep_count_fli_stat_li=[]

# Print results.
for row in rows:
    dep_fli_stat_li.append(row[0])
    dep_airport_to_li.append(row[1])
    dep_count_fli_stat_li.append(row[2])


df_dep_flight_stat_count=pd.DataFrame({
    'dep_fli_stat_li': dep_fli_stat_li,
    'dep_airport_to_li':dep_airport_to_li,
    'dep_count_fli_stat_li':dep_count_fli_stat_li
})



fig_dep_flights_stat_count = px.bar(df_dep_flight_stat_count, x='dep_airport_to_li', y='dep_count_fli_stat_li',color='dep_fli_stat_li', title="Delay in Departure")
#fig.show()
st.plotly_chart(fig_dep_flights_stat_count)

####################avg delay arr per airport ##############################
rows=run_query(
"""select airport_to, avg(arr_delay_mins) 
from (
select airport_to,arr_act,arr_sch, abs(SUBTIME(arr_sch,arr_act ) )/100 as arr_delay_mins   # #,AVG() as avg_arr_delay
from fli_data_table
where arr_act != '-- ' AND arr_act != '-- '
and arr_sch<arr_act #late
)t1
group by airport_to"""
)


dep_airport_to_li=[]
avg_arr_delay_li=[]

# Print results.
for row in rows:
    dep_airport_to_li.append(row[0])
    avg_arr_delay_li.append(row[1])
    


df_dep_flight_stat_count=pd.DataFrame({
    'dep_airport_to_li': dep_airport_to_li,
    'avg_arr_delay_li':avg_arr_delay_li
})

labels = dep_airport_to_li#each_airline


# Use `hole` to create a donut-like pie chart
fig_avg_arr_delay = go.Figure(data=[go.Pie(labels=labels, values=avg_arr_delay_li, hole=.3,title="AVG arrival delay")])
st.subheader("Avg Arrival Delay for each Airport")
st.plotly_chart(fig_avg_arr_delay)

#############avg delay arr and dep##############################
rows=run_query(
"""
select t3.airport_to,IFNULL(dep_delay,0) as dep_d,IFNULL(arr_delay,0)  as arr_d
 from(
	select airport_to, avg(arr_delay_mins)  as arr_delay
	from (
	select airport_to,arr_act,arr_sch, abs(SUBTIME(arr_sch,arr_act ) )/100 as arr_delay_mins ,id  # #,AVG() as avg_arr_delay
	from fli_data_table
	where arr_act != '-- ' AND arr_act != '-- '
	and arr_sch<arr_act #late
	)t1
	group by airport_to
    )t3
left OUTER JOIN
  (
	select airport_to, avg(dep_delay_mins)  as dep_delay
	from (
	select airport_to,dep_act,dep_sch, abs(SUBTIME(dep_sch,dep_act ) )/100 as dep_delay_mins,id   # #,AVG() as avg_arr_delay
	from fli_data_table
	where arr_act != '-- ' AND arr_act != '-- '
	and dep_sch<dep_act #late
	)t2
	group by airport_to
  )t4
ON t4.airport_to=t3.airport_to



"""
)

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

fig_avg_dep_arr= go.Figure(data=[
    go.Bar(name='avg dep delay', x=dep_airport_to_li, y=avg_dep_delay_li),
    go.Bar(name='avg arr delay', x=dep_airport_to_li, y=avg_arr_delay_li)
])

fig_avg_dep_arr.update_layout(barmode='group')
st.plotly_chart(fig_avg_dep_arr)






