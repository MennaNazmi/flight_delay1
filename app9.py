from lxml import html
import requests
import json
import html_to_json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import html_to_json
import urllib.request
import re

link = requests.get('https://www.flightstats.com/v2/flight-tracker/departures/CAI/?year=2021&month=9&date=13&hour=0')


src=link.content 

soup=BeautifulSoup(src,"html.parser")

print( re.findall("<script>(.*?)</script>", link.text, re.DOTALL))

all_data= re.findall("<script>(.*?)</script>", link.text, re.DOTALL)


#src_html=link.content
#src_json=src_html.json(link.decode('utf-8'))
#print(link.text.find("_NEXT_DATA_"))




#data = json.loads(src_html)
#print(data)
#data_fil=data['html']['body']['script']['_value']
#print(data['html']['body']['script']['_value'])
#output_json = html_to_json.convert(src_html)
#print(output_json)
#with open('data.json', 'w') as f:
 #   json.dump(data['html']['body']['script']['_value'], f)
#print(src_json['html']['body']['script']['_value'])
#if output_json.keys() =='script' :
#    print(output_json.items())








