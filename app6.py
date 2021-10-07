## getting data from web then upload it to database mysql
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



links=[]


#results_CAI_page=requests.get("https://www.flightstats.com/v2/flight-tracker/departures/CAI")

#src=results_CAI_page.content 

#soup=BeautifulSoup(src,"html.parser")


with open('fli_data/fli2.csv', 'r') as file:
    reader = csv.reader(file)
    #data = list(reader) 
    for row in reader:
        #print(row[2])
        if len(links)==4 : break
        links.append(row[2])

links_list=list(filter(None,links))
print(len(links_list))





dep_sch_list=[]
dep_act_list=[]
arr_sch_list=[]
arr_act_list=[]
flight_from_list=[]
flight_to_list=[]
flight_from_airport_li=[]
flight_to_airport_li=[]
time_stat_li=[]
flight_code_li=[]
flight_date_li=[]
from_dep_li=[]
flight_status_li=[]
#to get into each link and get the data
for link_each_page in range(1,len(links_list)):
    results_link=requests.get(links_list[link_each_page])
    src=results_link.content 
    #print(src)
    soup=BeautifulSoup(src,"html.parser")
    sched_depart=soup.find_all("div",{"class":"text-helper__TextHelper-sc-8bko4a-0 kbHzdx"})
    flight=soup.find_all("div",{"class":"text-helper__TextHelper-sc-8bko4a-0 efwouT"})
    flight_airport=soup.find_all("div",{"class":"text-helper__TextHelper-sc-8bko4a-0 cHdMkI"})
    flight_code=soup.find_all("div",{"class":"text-helper__TextHelper-sc-8bko4a-0 OvgJa"})
    flight_date=soup.find_all("div",{"class":"text-helper__TextHelper-sc-8bko4a-0 cPBDDe"})
    flight_status=soup.find_all("div",{"class":"text-helper__TextHelper-sc-8bko4a-0 iicbYn"})
    if flight_status[0].text in ['Arrived']:
       flight_link_fordetails=soup.find_all("a",{"class":"button-link__ButtonLink-sc-wcss74-0 dVTZZ"})
       details_link=flight_link_fordetails[3].get('href')
       ##inside the link to get the weather wind 
       res_detailed_link=requests.get(details_link)
       src1=res_detailed_link.content 
       soup1=BeautifulSoup(src1,"html.parser")
       weather=soup1.find_all("div",{"class":"sc-frDJqD bMlduJ"})


       print(weather)
    from_dep_li.append("CAI")
    flight_date_li.append(flight_date[0].text)
    flight_code_li.append(flight_code[0].text)
    #time_stat=soup.find_all("div",{"class":"text-helper__TextHelper-sc-8bko4a-0 feVjck"})    
    flight_from_list.append(flight[0].text)
    flight_to_list.append(flight[1].text)
    flight_from_airport_li.append(flight_airport[0].text)
    flight_to_airport_li.append(flight_airport[1].text)
     #time_stat_li.append(time_stat[0].text)
    #print(time_stat[0].text)
    dep_sch_list.append(sched_depart[0].text)
    #print(links_list[link_each_page])
    print(sched_depart[0].text)
    dep_act_list.append(sched_depart[1].text)
    arr_sch_list.append(sched_depart[2].text)
    arr_act_list.append(sched_depart[3].text)
    flight_status_li.append(flight_status[0].text)
   # print(flight_airport[1].text)
print(flight_status_li)
print("#########")

#print(flight_from_airport_li)
###############################put lists in database

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="vegatry1",
    database="flaskapp"
)


#button-link__ButtonLink-sc-wcss74-0 dVTZZ


#mycursor=mydb.cursor(buffered=True) 
#print(from_dep_li)

#for i in range(len(flight_code_li)):
   # print(len(flight_code_li))
#(flight_code_li[0],flight_date[0],from_dep[0],flight_from_list[0],flight_to_list[0],flight_from_airport_li[0],flight_to_airport_li[0],dep_sch_list[0],dep_act_list[0],arr_sch_list[0],arr_act_list[0])
#    mycursor.execute("INSERT INTO fli_data_table(flight_code,flight_date,from_dep,flight_from,flight_to,airport_from,airport_to,dep_sch,dep_act,arr_sch,arr_act) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(	flight_code_li[i]	,flight_date_li[i]	,from_dep_li[i]	,flight_from_list[i],	flight_to_list[i],	flight_from_airport_li[i]	,flight_to_airport_li[i],	dep_sch_list[i]	,dep_act_list[i],	arr_sch_list[i]	,arr_act_list[i]))
   
    #print(flight_date_li[i])
#mydb.commit()
#mycursor.close()

######################get data from database########################
#mycursor.execute()
#myres=mycursor.fetchall()

#df=pd.DataFrame(myres,columns=['flight_code','flight_date','from_dep','flight_from','flight_to','airport_from','airport_to','dep_sch','dep_act','arr_sch','arr_act','id'])
#for row in myres:

#def run_query(query):
#    with mydb.cursor() as cur:
#        cur.execute(query)
#        return cur.fetchall()

#rows = run_query("Select * from fli_data_table")
#for row in rows:
    #print(row)
