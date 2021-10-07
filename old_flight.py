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
#st.title("HOLA ")

#st.header("Header")
#st.subheader("subheader")
#st.text("this is a text")
#st.markdown(""" # h1 tag 
## h2 tag 
### h3 """)

#app= Flask(__name__)

#@app.route("/")
#def index():
#    return render_template('index.html')
# https://airportcod.es/#  airline codes

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="vegatry1",
    database="flaskapp"
)


mycursor=mydb.cursor(buffered=True) 
csv_data=csv.reader(open('fli_data/mini_flight.csv'))
data_list=list(csv_data)
statment="INSERT INTO flight_table(year_,month_,day_,day_of_week,airline,flight_number,tail_number,origin_airport,destination_airport,scheduled_departure,departure_time,departure_delay,taxi_out,wheels_off,scheduled_time,elapsed_time,air_time,distance,wheels_on,taxi_in,scheduled_arrival,arrival_time,arrival_delay) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#PUTTING the data into database MYSQL 
#for row in data_list[1:]:
#    mycursor.execute("INSERT INTO flight_table(year_,month_,day_,day_of_week,airline,flight_number,tail_number,origin_airport,destination_airport,scheduled_departure,departure_time,departure_delay,taxi_out,wheels_off,scheduled_time,elapsed_time,air_time,distance,wheels_on,taxi_in,scheduled_arrival,arrival_time,arrival_delay) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row))
#mydb.commit()
#mycursor.close()



#get data from database 
mycursor.execute("Select year_,month_,day_,day_of_week,airline,flight_number,tail_number,origin_airport,destination_airport,scheduled_departure,departure_time,departure_delay,taxi_out,wheels_off,scheduled_time,elapsed_time,air_time,distance,wheels_on,taxi_in,scheduled_arrival,arrival_time,arrival_delay from flight_table")
myres=mycursor.fetchall()

df=pd.DataFrame(myres,columns=['year_','month_','day_','day_of_week','airline','flight_number','tail_number','origin_airport','destination_airport','scheduled_departure','departure_time','departure_delay','taxi_out','wheels_off','scheduled_time','elapsed_time','air_time','distance','wheels_on','taxi_in','scheduled_arrival','arrival_time','arrival_delay'])
#for row in myres:
df_sch_act_dep=df['scheduled_departure'],df['departure_time']
distinct_airline=df.airline.unique() #without comma
print("KKKKKKKKKKKK")
print(distinct_airline) 
print("YYYYYYYYYY")
#st.line_chart(df['departure_delay'] )
#st.area_chart(df['departure_delay'] )
#st.bar_chart(df['distance'] )
st.title("Flight Dashboard")
if st.button('Hit me'):
    st.write("how btn works")
#st.checkbox('Check me out')
#st.radio('Radio', [1,2,3])






def run_query(query):
    with mydb.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("select count(flight_number),airline from flight_table group by airline;")
number_flights=[]
each_airline=[]
# Print results.
for row in rows:
    number_flights.append(row[0])
    each_airline.append(row[1])
    #st.write(f"{row[0]} has a :{row[1]}:")
#print(number_flights)
#print(each_airline)

#st.write("Here's our first attempt at using data to create a table:")

flights_each_airline=pd.DataFrame({
    'number_of_flights': number_flights,
    'airline': each_airline
})
#st.table(chart_data)
fig=px.bar(flights_each_airline,x="number_of_flights", y="airline",orientation='h',title='Number of Flights Each Airline')
st.plotly_chart(fig)

#each_airline.append("<select>")

#selection_value=st.selectbox('Select The Airline',each_airline,14)#airline
#if selection_value=="AS":
#    st.write(f"u choose selection_value ={selection_value} ")
#elif selection_value=="AS" :
#    st.write(f"u choose selection_value ={selection_value} ")
#elif selection_value=="US" :
#    st.write(f"u choose selection_value ={selection_value} ")
#elif selection_value=="DL" :
#    st.write(f"u choose selection_value ={selection_value} ")
#elif selection_value=="NK" :
#    st.write(f"u choose selection_value ={selection_value} ")
#elif selection_value=="UA" :
#    st.write(f"u choose selection_value ={selection_value} ")
#elif selection_value=="HA" :
#    st.write(f"u choose selection_value ={selection_value} ")
#elif selection_value=="B6" :
#    st.write(f"u choose selection_value ={selection_value} ")
#elif selection_value=="OO" :
#    st.write(f"u choose selection_value ={selection_value} ")
#elif selection_value=="EV" :
#    st.write(f"u choose selection_value ={selection_value} ")
#elif selection_value=="MQ" :
#    st.write(f"u choose selection_value ={selection_value} ")
#elif selection_value=="F9" :
#    st.write(f"u choose selection_value ={selection_value} ")
#elif selection_value=="MN" :
#    st.write(f"u choose selection_value ={selection_value} ")
#elif selection_value=="VX" :
#    st.write(f"u choose selection_value ={selection_value} ")
#else :









##########get the data from MYSQL
rows = run_query("select avg(air_time),avg(distance),airline from flight_table group by airline")
avg_air_time=[]
avg_distance=[]
each_airline=[]
# Print results.
for row in rows:
    avg_air_time.append(row[0])
    avg_distance.append(row[1])
    each_airline.append(row[2])
###create DATAframe of the DATA that we get from MYSQL 
avg_air_time_each_airline=pd.DataFrame({
    'number_of_flights': avg_air_time,
    'avg_distance': avg_distance,
    'airline': each_airline
})


####PLOT
#each_airline

fig_avgairtime_avg_dist = go.Figure(data=[
    go.Bar(name='avg_air_time', x=each_airline, y=avg_air_time),
    go.Bar(name='avg_distance', x=each_airline, y=avg_distance)
])
# Change the bar mode
fig_avgairtime_avg_dist.update_layout(barmode='group')
#fig.show()

st.subheader("Avg airtime and Avg Distance")
st.plotly_chart(fig_avgairtime_avg_dist)








rows = run_query("select  avg(departure_delay),  airline  from flight_table group by airline")
avg_dep_delay=[]
each_airline=[]
# Print results.
for row in rows:
    avg_dep_delay.append(row[0])
    each_airline.append(row[1])
###create DATAframe of the DATA that we get from MYSQL 
avg_air_time_each_airline=pd.DataFrame({
    'avg_dep_delay': avg_dep_delay,
    'airline': each_airline
})


####PLOT
#each_airline
labels = each_airline#each_airline


# Use `hole` to create a donut-like pie chart
fig_avg_dep_delay = go.Figure(data=[go.Pie(labels=labels, values=avg_dep_delay, hole=.3)])
st.subheader("Avg Departure Delay for each Air Line")

#fig.show()
st.plotly_chart(fig_avg_dep_delay)

##################
######################################



rows = run_query("select avg(taxi_out),avg(taxi_in) ,airline from flight_table group by airline")
taxi_out=[]
taxi_in=[]
airline=[]
# Print results.
for row in rows:
    taxi_out.append(row[0])
    taxi_in.append(row[1])
    airline.append(row[2])
###create DATAframe of the DATA that we get from MYSQL 
taxi_out_in_airline=pd.DataFrame({
    'taxi_out': taxi_out,
    'taxi_in':taxi_in,
    'airline': airline
})




fig_taxi_in_out = px.bar(taxi_out_in_airline, x="airline", y=["taxi_in", "taxi_out"], title="Taxi In and Taxi Out")

st.plotly_chart(fig_taxi_in_out)
#######################################
col1, col2 = st.columns(2)
col1.metric("Early Time","05:24:66", "00:03:24 mins")
col2.metric("Delay Time","06:23:66", "-00:02:09 mins")







rows = run_query("select id,airline,scheduled_departure,departure_time,scheduled_arrival,arrival_time,arrival_delay,departure_delay  from flight_table limit 100")


id=[]
airline=[]
scheduled_departure=[]
departure_time=[]
scheduled_arrival=[]
arrival_time=[]
arrival_delay=[]
departure_delay=[]

# Print results.
for row in rows:
    id.append(row[0])
    airline.append(row[1])
    scheduled_departure.append(row[2])
    departure_time.append(row[3])
    scheduled_arrival.append(row[4])
    arrival_time.append(row[5])
    arrival_delay.append(row[6])
    departure_delay.append(row[7])

   
###create DATAframe of the DATA that we get from MYSQL 
data_side_bar=pd.DataFrame({
    'id': id,
    'airline': airline,
    'scheduled_departure':scheduled_departure,
    'departure_time':departure_time,
    'scheduled_arrival':scheduled_arrival,'arrival_time':arrival_time,
    'arrival_delay':arrival_delay,'departure_delay':departure_delay
})



all_col=data_side_bar.columns

nav_page= st.sidebar.radio("Navigation",["Home","About Us"])

if nav_page=="Home":
    choose_airline_with_nothing=data_side_bar.airline.unique()
    #choose_airline_with_nothing.append("<select>")
    choose_airline=st.sidebar.selectbox("select the airline",choose_airline_with_nothing)
##plot with specific airline like each delay
    multiselect_col=st.sidebar.multiselect("select col",all_col) 
    st.title(choose_airline)
    st.subheader(f"u choose  {multiselect_col} from {choose_airline}")
    
    #st.area_chart(multiselect_col)
    
    #st.line_chart(multiselect_col)

if nav_page=="About Us":
    st.header("we are Vega")
    vid_file=open("flight.mp4","rb").read()
    st.video(vid_file)
    image = Image.open('airplane-flight.jpg')
    st.image(image, caption='plane')




#st.multiselect('Multiselect Months', [1,2,3]) 
#st.slider('Slide me', min_value=0, max_value=10)
#st.select_slider('Slide to select', options=[1,'2'])
#welc_name=st.text_input('please Enter your name')
#st.write("Welcome ", welc_name)
#st.number_input('Enter a number')
#st.text_area('Area for textual entry')
#st.date_input('Date input')
#st.time_input('Time entry')

#if __name__ == '__main__':
 #   app.run(debug=True)
