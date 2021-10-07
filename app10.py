#put data in mysql
import json
#import r
import json
import requests
import urllib.request
#import xmltojson
import html_to_json
import pandas as pd
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

src  = requests.get("https://www.flightstats.com/v2/flight-tracker/departures/CAI/?year=2021&month=9&date=19&hour=0")
#src  = requests.get("https://www.flightstats.com/v2/flight-tracker/departures/CAI/?year=2021&month=9&date=17&hour=0")

all_data=src.text
#print(all_data)
start_sector =all_data.find("__NEXT_DATA__ = ") + len("__NEXT_DATA__ = ")##start index ends
end_sector = all_data.find("module=")
sub_data = all_data[start_sector:end_sector].strip()
#print(sub_data)


data_to_json_format=json.loads(sub_data) 
flight_data=data_to_json_format['props']['initialState']['flightTracker']['route']['flights']
#print(flight_data)


#file = open("sample2.html","w")
#file.write(sub_data)
#file.close()



#SAVE IN JSON FILE 
with open("sample2.json", "w") as outfile:
    json.dump(flight_data, outfile)
    
sortime_li=[]
dep_time=[]
arr_time=[]
carrier_fs=[]
carrier_name=[]
carrier_flightnumber=[]
url_li=[]
url_li2=[]
airport_fs=[]
airport_city=[]


#for loop to get the flight_list
for index in  range(len(flight_data)):
   
   #for key in flight_data[index]:
    #  print(flight_data[index][key])
   sortime_li.append(flight_data[index]['sortTime'])
   dep_time.append(flight_data[index]['departureTime']['time24'])
   arr_time.append(flight_data[index]['arrivalTime']['time24'])
   carrier_fs.append(flight_data[index]['carrier']['fs'])
   carrier_name.append(flight_data[index]['carrier']['name'])
   carrier_flightnumber.append(flight_data[index]['carrier']['flightNumber'])
   url_li.append(flight_data[index]['url'])
   airport_fs.append(flight_data[index]['airport']['fs'])
   airport_city.append(flight_data[index]['airport']['city'])
   url_li2.append("https://www.flightstats.com/v2"+url_li[index])
#we have the whole table in list
#lets upload them in MYSQL
#print(url_li2)

###############detailed page###############


flight_details_li=[]
cancel_var_li=[]
landed_var_li=[]
dep_actual_li=[]
dep_scheduled_li=[]
arr_actual_li=[]
arr_scheduled_li=[]
delay_dep_li=[]
delay_arr_li=[]
dep_airport_name_li=[]
arr_airport_name_li=[]
flight_type_li=[]
flight_duration_li=[]
flight_tail_li=[]
flight_details_li=[]
for i in url_li2:
    #print(i)
    src  = requests.get(i)
    all_data=src.text
    start_sector =all_data.find("__NEXT_DATA__ = ") + len("__NEXT_DATA__ = ")##start index ends
    end_sector = all_data.find("module=")
    sub_data = all_data[start_sector:end_sector].strip()
#print(sub_data)

    data_to_json_format=json.loads(sub_data) 
    cancel_var=data_to_json_format['props']['initialState']['flightTracker']['flight']['flightNote']['canceled'] #['initialState']['flightTracker']['route']['flights']
    cancel_var_li.append(cancel_var)

    landed_var=data_to_json_format['props']['initialState']['flightTracker']['flight']['flightNote']['landed'] #['initialState']['flightTracker']['route']['flights']
    landed_var_li.append(landed_var)

    dep_actual=data_to_json_format['props']['initialState']['flightTracker']['flight']['schedule']['estimatedActualDeparture']
    dep_actual_li.append(dep_actual)
    
    dep_scheduled=data_to_json_format['props']['initialState']['flightTracker']['flight']['schedule']['scheduledDeparture']
    dep_scheduled_li.append(dep_scheduled)

    arr_actual=data_to_json_format['props']['initialState']['flightTracker']['flight']['schedule']['estimatedActualArrival']
    arr_actual_li.append(arr_actual)
    #print(arr_actual_li)

    arr_scheduled=data_to_json_format['props']['initialState']['flightTracker']['flight']['schedule']['scheduledArrival']
    arr_scheduled_li.append(arr_scheduled)
    
    delay_dep=data_to_json_format['props']['initialState']['flightTracker']['flight']['status']['delay']['departure']['minutes']
    delay_dep_li.append(delay_dep)
    
    delay_arr=data_to_json_format['props']['initialState']['flightTracker']['flight']['status']['delay']['arrival']['minutes']
    delay_arr_li.append(delay_arr)

    dep_airport_name=data_to_json_format['props']['initialState']['flightTracker']['flight']['departureAirport']['name']
    dep_airport_name_li.append(dep_airport_name)
    
    arr_airport_name=data_to_json_format['props']['initialState']['flightTracker']['flight']['arrivalAirport']['name']
    arr_airport_name_li.append(arr_airport_name)
    
    flight_type=data_to_json_format['props']['initialState']['flightTracker']['flight']['additionalFlightInfo']['equipment']['name']
    flight_type_li.append(flight_type)

    flight_duration=data_to_json_format['props']['initialState']['flightTracker']['flight']['additionalFlightInfo']['flightDuration']
    flight_duration_li.append(flight_duration)
    #flight_duration=data_to_json_format['props']['initialState']['flightTracker']['flight']['additionalFlightInfo']['equipment']['flightDuration']

    flight_tail=data_to_json_format['props']['initialState']['flightTracker']['flight']['positional']['flexTrack']['tailNumber']
    flight_tail_li.append(flight_tail)
    #flight_details_li.extend(cancel_var,landed_var,dep_actual,dep_scheduled,arr_actual,arr_scheduled,delay_dep,delay_arr,dep_airport_name,arr_airport_name,flight_type,flight_duration,flight_tail)

#flight_details_li_alias=['cancel_var','landed_var','dep_actual','dep_scheduled','arr_actual','arr_scheduled','delay_dep','delay_arr','dep_airport_name','arr_airport_name','flight_type','flight_duration','flight_tail']

#flight_details_li=[cancel_var,landed_var,dep_actual,dep_scheduled,arr_actual,arr_scheduled,delay_dep,delay_arr,dep_airport_name,arr_airport_name,flight_type,flight_duration,flight_tail]

#print(flight_details_li_alias)
#print(cancel_var,landed_var,dep_actual,dep_scheduled,arr_actual,arr_scheduled,delay_dep,delay_arr,dep_airport_name,arr_airport_name,flight_type,flight_duration,flight_tail)






################################################
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="vegatry1",
    database="flaskapp"
)


mycursor=mydb.cursor(buffered=True) 
for i in range(len(carrier_name)):
    mycursor.execute("INSERT INTO flight_t2(sortTime,departureTime,arrivalTime,carrier_fs,carrier_name,carrier_fn,url,airport_fs,airport_city,cancel_var,landed_var,dep_actual,dep_scheduled,arr_actual,arr_scheduled,delay_dep,delay_arr,dep_airport_name,arr_airport_name,flight_type,flight_duration,flight_tail) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(sortime_li[i],dep_time[i],arr_time[i],carrier_fs[i],carrier_name[i],carrier_flightnumber[i],url_li2[i],airport_fs[i],airport_city[i],cancel_var_li[i],landed_var_li[i],dep_actual_li[i],dep_scheduled_li[i],arr_actual_li[i],arr_scheduled_li[i],delay_dep_li[i],delay_arr_li[i],dep_airport_name_li[i],arr_airport_name_li[i],flight_type_li[i],flight_duration_li[i],flight_tail_li[i]))
mydb.commit()
 #  print(carrier_flightnumber[i])
mycursor.close()

#mycursor=mydb.cursor(buffered=True) 
#mycursor.execute("INSERT INTO flight_t2(cancel_var,landed_var,dep_actual,dep_scheduled,arr_actual,arr_scheduled,delay_dep,delay_arr,dep_airport_name,arr_airport_name,flight_type,flight_duration,flight_tail)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(cancel_var_li[0],landed_var_li[0],dep_actual_li[0],dep_scheduled_li[0],arr_actual_li[0],arr_scheduled_li[0],delay_dep_li[0],delay_arr_li[0],dep_airport_name_li[0],arr_airport_name_li[0],flight_type_li[0],flight_duration_li[0],flight_tail_li[0]))
#mydb.commit()
print("DDDDDDDDDD")













#with open('sample.json') as json_file:
#    data = json.load(json_file)
  
    # Print the type of data v
    #print("Type:", data)
    #print("_value':", data['_value'])

#    print(data)