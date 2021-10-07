import requests

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest 


results_CAI_page=requests.get("https://www.flightstats.com/v2/flight-tracker/departures/CAI")

src=results_CAI_page.content 

soup=BeautifulSoup(src,"html.parser")
#print(soup) 

#print(flight_nav1)

#html_page = urlopen("https://www.flightstats.com/v2/flight-tracker/departures/CAI")
#soup = BeautifulSoup(html_page,"html.parser")
flight_name=soup.find_all("div",{"class":"table__Cell-sc-1x7nv9w-13 xYLPe"})
dest_name=soup.find_all("div",{"class":"table__Cell-sc-1x7nv9w-13 dMgArR"})
for_links=soup.find_all("a",{"class":"table__A-sc-1x7nv9w-2 hnJChl"})
#flight_name2=soup.find_all("span",{"class":"table__SubText-sc-1x7nv9w-16 bQPdJx"})
#for_links[2].attrs={'href': re.compile("^https://")}
#print(flight_name2)
flight_name2=soup.find_all("div",{"class":"table__Cell-sc-1x7nv9w-13 bUfMgp"})
dest_name2=soup.find_all("div",{"class":"table__Cell-sc-1x7nv9w-13 dMgArR"})

 



#print("https://www.flightstats.com"+for_links[2].get('href'))
#print(for_links[2])
dest_list=[]
flight_list=[]
links_list=[]
flight_name2_list=[]
dest_name2_list=[]
#print(len(for_links))
#to exetrract exact txt without a or div
for i in range (len(flight_name)):
    flight_list.append(flight_name[i].text)
    dest_list.append(dest_name[i].text)

for i in range (len(flight_name2)):
    flight_name2_list.append(flight_name2[i].text)
    dest_name2_list.append(dest_name2[i].text)
    #print(len(flight_name2))
    #print(flight_name2[i].text)
    #flight_name2_list.append(flight_name2[i].text)
    #print(len(flight_name2_list))

for i in range (len(for_links)): 
    links_list.append("https://www.flightstats.com"+for_links[i].get('href'))
    

links_list.insert(0, "Links")



dep_sch_list=[]
dep_act_list=[]
arr_sch_list=[]
arr_act_list=[]
#to get into each link and get the data
for link_each_page in range(1,len(links_list)):
    results_link=requests.get(links_list[link_each_page])
    src=results_link.content 
    soup=BeautifulSoup(src,"html.parser")
    sched_depart=soup.find_all("div",{"class":"text-helper__TextHelper-sc-8bko4a-0 kbHzdx"})
    dep_sch_list.append(sched_depart[0].text)
    dep_act_list.append(sched_depart[1].text)
    arr_sch_list.append(sched_depart[2].text)
    arr_act_list.append(sched_depart[3].text)
print(len(links_list))
    #flight_time_dist_eq=soup.find_all("h4",{"class":"labeled-columns__Label-sc-j3eq63-0 fFaZrb"})
    #for each_flight_detail in flight_time_dist_eq:
        #print(each_flight_detail.text)
        #print(len(flight_time_dist_eq))
        #print ("######")
    #print(flight_time_dist_eq[0].text)
    #print(flight_time_dist_eq[1].text)
    #print(flight_time_dist_eq[2].text)
    #print(flight_time_dist_eq[3].text)
    #print( flight_time_dist_eq[4].text)
    #print(flight_time_dist_eq[5].text)
    #print(flight_time_dist_eq[6].text)
    #print(flight_time_dist_eq[7].text)
    #print(sched_depart[0].text)#departure scheduled 
    #print(sched_depart[1].text)#departure actual 
    #print(sched_depart[2].text)#arrival scheduled
    #print(sched_depart[3].text)#arrival actual
    
    #sched_depart_list.append(sched_depart)

#print(len(sched_depart))

#print(dep_sch_list)
















#print(links)
#print(for_links[1])
#print(flight_list)
#print(dest_list)
    
#save in file





dep_sch_list.insert(0, "dep_sch_time")
dep_act_list.insert(0, "dep_act_time")
arr_sch_list.insert(0, "arr_sch_time")
arr_act_list.insert(0, "arr_act_time")
flight_name2_list.insert(0,"flight_name2")
dest_name2_list.insert(0,"dest_name2")

file_list=[flight_list,dest_list,links_list,dep_sch_list,dep_act_list,arr_sch_list,arr_act_list,flight_name2_list,dest_name2_list]
unpacking_list=zip_longest(*file_list)


#with open("fli_data/fli3.csv","w") as myfile: 
   # w_object=csv.writer(myfile)
    #w_object.writerow(["flight_name","destination_name"])
   # w_object.writerows(unpacking_list)





#for link in soup.findAll('a'):
 #   print (link.get('href'))

#flight_name1=soup.find_all("a",{"class":"table__A-sc-1x7nv9w-2 hnJChl"})

#find_all_a =soup.find_all("a", href=True)
#print(flight_name1)


#print(flight_name1)
#flight_name1.find_all("a",href='TRUE')
#for i in range(len(flight_name1)):
#    #get the link in the section
 #   links.append(flight_name1[i].find("a").attrs['href'])
 #   print(links)



#rows=flight1.find_all("h2",{"class":"table__CellText-sc-1x7nv9w-15 fcTUax"})

#flight_name1
#flight_name2=soup.find_all("h2",{"class":"table__CellText-sc-1x7nv9w-15 fcTUax"})

#dest_name1=soup.find_all("div",{"class":"table__Cell-sc-1x7nv9w-13 bUfMgp"})
#dest_name2=soup.find_all("div",{"class":"table__Cell-sc-1x7nv9w-13 dMgArR"})
###################################################3

