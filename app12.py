#getting details for each link (flight)
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

src  = requests.get("https://www.flightstats.com/v2/flight-tracker/MS/901?year=2021&month=9&date=17&flightId=1070843994")
#src  = requests.get("https://www.flightstats.com/v2/flight-tracker/departures/CAI/?year=2021&month=9&date=17&hour=0")

all_data=src.text
#print(all_data)
start_sector =all_data.find("__NEXT_DATA__ = ") + len("__NEXT_DATA__ = ")##start index ends
end_sector = all_data.find("module=")
sub_data = all_data[start_sector:end_sector].strip()
#print(sub_data)

data_to_json_format=json.loads(sub_data) 
cancel_var=data_to_json_format['props']['initialState']['flightTracker']['flight']['flightNote']['canceled'] #['initialState']['flightTracker']['route']['flights']
landed_var=data_to_json_format['props']['initialState']['flightTracker']['flight']['flightNote']['landed'] #['initialState']['flightTracker']['route']['flights']

dep_actual=data_to_json_format['props']['initialState']['flightTracker']['flight']['schedule']['estimatedActualDeparture']
dep_scheduled=data_to_json_format['props']['initialState']['flightTracker']['flight']['schedule']['scheduledDeparture']

arr_actual=data_to_json_format['props']['initialState']['flightTracker']['flight']['schedule']['estimatedActualArrival']
arr_scheduled=data_to_json_format['props']['initialState']['flightTracker']['flight']['schedule']['scheduledArrival']

delay_dep=data_to_json_format['props']['initialState']['flightTracker']['flight']['status']['delay']['departure']['minutes']
delay_arr=data_to_json_format['props']['initialState']['flightTracker']['flight']['status']['delay']['arrival']['minutes']

dep_airport_name=data_to_json_format['props']['initialState']['flightTracker']['flight']['departureAirport']['name']
arr_airport_name=data_to_json_format['props']['initialState']['flightTracker']['flight']['arrivalAirport']['name']
flight_type=data_to_json_format['props']['initialState']['flightTracker']['flight']['additionalFlightInfo']['equipment']['name']

flight_duration=data_to_json_format['props']['initialState']['flightTracker']['flight']['additionalFlightInfo']['flightDuration']
#flight_duration=data_to_json_format['props']['initialState']['flightTracker']['flight']['additionalFlightInfo']['equipment']['flightDuration']

flight_tail=data_to_json_format['props']['initialState']['flightTracker']['flight']['positional']['flexTrack']['tailNumber']


print(cancel_var)
print(landed_var)
print(dep_actual)
print(dep_scheduled)
print(arr_actual)
print(arr_scheduled)
print(delay_dep)
print(delay_arr)
print(dep_airport_name)
print(arr_airport_name)
print(flight_type)
print(flight_duration)
print(flight_tail)
#flight_details_li_alias=['cancel_var','landed_var','dep_actual','dep_scheduled','arr_actual','arr_scheduled','delay_dep','delay_arr','dep_airport_name','arr_airport_name','flight_type','flight_duration','flight_tail']

flight_details_li=[cancel_var,landed_var,dep_actual,dep_scheduled,arr_actual,arr_scheduled,delay_dep,delay_arr,dep_airport_name,arr_airport_name,flight_type,flight_duration,flight_tail]

#print(flight_details_li_alias)
print(flight_details_li)
#SAVE IN JSON FILE 
#with open("s3.json", "w") as outfile:
 #   json.dump(flight_data, outfile)
