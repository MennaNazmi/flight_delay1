import urllib.request
#import r
import json
import requests
#import xmltojson
import html_to_json
import pandas as pd
url  = "https://www.flightstats.com/v2/flight-tracker/departures/CAI/?year=2021&month=9&date=13&hour=0"
page = requests.get(url)
html_data = page.text

print(html_data)
output_json = html_to_json.convert(html_data)
print(output_json)

#with open('data.json', 'w') as f:
#    json.dump(output_json, f)
#json_ = xmltojson.parse(html_data)
with open("file.txt", "r",encoding='utf-8') as code:
    file=code.read()
    start_link = file.find(' _NEXT_DATA_ =')
    end_quote = file.find('module', start_link)
    target = file[start_link+len(' _NEXT_DATA_ ='):end_quote].strip()
    convert = json.loads(target)
    file=code.read()
    start_link = file.find(' _NEXT_DATA_ =')
    end_quote = file.find('module', start_link)
    target = file[start_link+len(' _NEXT_DATA_ ='):end_quote].strip()

#flight_info=convert['props']['initialState']['flightTracker']['route']['flights'][2]