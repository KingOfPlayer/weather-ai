from asyncio import Condition
from inspect import currentframe
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import re
import json
from datetime import datetime
from datetime import timedelta

def skipcookieSite():
    ##setup site settings

    #cookie accept
    cookie_modal = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID,"cookieModal")))
    cookies_accept_button = cookie_modal.find_element(By.XPATH,"//button[text()='Accept']")
    cookies_accept_button.click()


def loadDataset(name):
    loaddataset = open('{}.json'.format(name), 'r')
    parsed_data = json.load(loaddataset)
    loaddataset.close()

    return parsed_data
  
def saveDataset(name, array):
    loaddataset = open('{}.json'.format(name), 'w+')
    loaddataset.truncate(0)
    loaddataset.write(json.dumps(array))
    loaddataset.close()

    print("Saved")


def nextDay():
    nextdaydate = datetime.strptime(driver.current_url.split('=',2)[-1].split('/',2)[0], "%Y-%m-%d") + timedelta(days=1)
    nextdaydatetext = nextdaydate.strftime("%Y-%m-%d")

    driver.get(f"{url_base}{nextdaydatetext}/{nextdaydatetext}")

    skipcookieSite()

def getTableData():
    global data
    url_date = driver.current_url.split('/',10)[-1]
    table_open_button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,"//button[@data-bs-target='#details-modal']")))
    table_open_button.click();
    modal_body = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,"//div[@id='details-modal']/div/div[@class='modal-content']/div[@class='modal-body']")))
    
    driver.implicitly_wait(1)

    epxpand_button = WebDriverWait(modal_body, 3).until(EC.presence_of_element_located((By.XPATH,"div[@class='d-flex align-items-center mt-2']//button")))
    epxpand_button.click()
    epxpand_button.click()

    tablebody = modal_body.find_element(By.XPATH,"//table/tbody")
    tablerows = tablebody.find_elements(By.XPATH,"tr")

    for index, tablerow in enumerate(tablerows, start=1):
        rowarray = tablerow.text.replace(u"\u00B0C", "").replace(u"\u2014", "").replace("mm", "").replace("km/h", "").replace("hPa", "").replace(u"\u0025", "").split()
        
        date = datetime.strptime(rowarray[0] + rowarray[1], "%Y-%m-%d%H").strftime("%Y-%m-%dT%H:%M:%S")
        temp = rowarray[2]
        dewPoint = rowarray[3]
        totalPrecipitation = rowarray[4]
        condition = tablerow.find_element(By.XPATH,"//td[1]/i").get_attribute("class").split("-",1)[1]
        windSpeed = rowarray[5]
        pressure = rowarray[6]
        humidity = rowarray[7]
        windDir = re.findall("\d+",tablerow.find_element(By.CSS_SELECTOR,"i.wi-wind").get_attribute("class"))[0]
        
        data.append([date,temp,dewPoint,totalPrecipitation,condition,windSpeed,pressure,humidity,windDir])

#main variables
data = []
url_base = "https://meteostat.net/en/station/LTBQ0?t="

#setup selenium
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 3)
driver.get("https://meteostat.net/en/station/LTBQ0?t=2024-11-01/2024-11-01")

skipcookieSite()

while True: 
    m = input("Mode? :")
    if m == "q":
        break;
    if m == "r":
        driver.refresh()
    if m == "n":
        nextDay()
    if m == "s":
        saveDataset(driver.current_url.split('/',10)[-2].split('?')[0], data);
    if m == "g":
        getTableData()
    if m == "auto":
        c = int(input("How many? : "))
        print("------------- Auto crawl started -------------")
        for i in range(c):
            print("------------- Auto crawl progress", i+1, "/", c, "-------------")
            getTableData()
            nextDay()
        print("------------- Done auto crawl -------------")
            
driver.close()