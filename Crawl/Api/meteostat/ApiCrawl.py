
from math import ceil
import time
import requests

import json
from datetime import datetime
from datetime import timedelta

def loadDataset(name):
    loaddataset = open('{}.json'.format(name), 'r')
    parsed_data = json.loads(loaddataset)
    loaddataset.close()

    return parsed_data
  
def saveDataset(name, array):
    loaddataset = open('{}.json'.format(name), 'w+')
    loaddataset.truncate(0)
    loaddataset.write(json.dumps(array))
    loaddataset.close()

    print("Saved")

def generateDayTable(year,mounth,day,dayCount):

    dayTable = []
    lastestdate = datetime.now()
    startdate = datetime(year,mounth,day);

    for x in range(0,dayCount,max_period):

        if(x+max_period>dayCount):
            nextdate = startdate + timedelta(days=dayCount)
        else:
            nextdate = startdate + timedelta(days=x+max_period)

        dayTable.append([(startdate + timedelta(days=x)).strftime("%Y-%m-%d"),nextdate.strftime("%Y-%m-%d")])

    return dayTable

def getData(dayTable):
    global data
    opsLeng = len(dayTable)
    for index, dayInterval in enumerate(dayTable, start=1):
        print(f"------------- {index}/{opsLeng} ------------- {dayInterval[0]} - {dayInterval[1]} -------------")
        r = requests.get(f"{base_url}&start={dayInterval[0]}&end={dayInterval[1]}")
        responseJSON = json.loads(r.content)
        for hourdata in responseJSON['data']:
            data.append([hourdata['time'].replace(" ", "T"),
                         hourdata['temp'],
                         hourdata['dwpt'],
                         hourdata['prcp'],
                         hourdata['coco'],
                         hourdata['wspd'],
                         hourdata['pres'],
                         hourdata['rhum'],
                         hourdata['wdir']])
        time.sleep(0.5)
    

data = []
max_period = 10
station = "LTBQ0"
base_url = f"https://d.meteostat.net/app/proxy/stations/hourly?station={station}&tz=Europe/Istanbul"

while True: 
    m = input("Mode? :")
    if m == "q":
        break;
    if m == "s":
        saveDataset(base_url.split("station=",1)[1].split("&",1)[0],data);
    if m == "g":
        year = int(input("Year?:"))
        month = int(input("Month?:"))
        day = int(input("Day?:"))
        count = int(input("Count?:"))
        dayTable = generateDayTable(year,month,day,count)
        print("------------- Crawl started -------------")
        getData(dayTable)
        print("------------- Crawl done -------------")
            