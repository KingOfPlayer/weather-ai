from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import json
from datetime import datetime
from datetime import timedelta

def setupSite():
    ##setup site settings

    #set driver wait
    

    #cookies
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='SP Consent Message']")))
    cookies_button = driver.find_element(By.XPATH,"//button[@class='message-component message-button no-children focusable cta-button sp_choice_type_11']")
    cookies_button.click()
    driver.switch_to.default_content()

    #temp type (Not work)
    # settings_button = wait.until(EC.visibility_of_element_located((By.ID,"wuSettings")))
    # settings_button.click()
    # celcius_button = driver.find_element(By.XPATH,"//a[@title='Switch to Metric']")
    # celcius_button.click()
    # driver.implicitly_wait(1)

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

def nextDay():
    global curdate
    curdate = curdate + timedelta(days=1)

    year = Select(driver.find_element(By.ID,"yearSelection"))
    year.select_by_index(abs(curdate.year-2024))
    month = Select(driver.find_element(By.ID,"monthSelection"))
    month.select_by_index(curdate.month-1)
    day = Select(driver.find_element(By.ID,"daySelection"))
    day.select_by_index(curdate.day-1)
    senddate_button = driver.find_element(By.ID,"dateSubmit")
    senddate_button.click()

    print("Next Day")

def getTableData():
    global data
    url_date = driver.current_url.split('/',10)[-1]

    tablebody = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='observation-table ng-star-inserted']/table/tbody")))
    tablerows = tablebody.find_elements(By.XPATH,"tr")
    for index, tablerow in enumerate(tablerows, start=1):
        entry = [];
        dateString = tablerow.find_element(By.XPATH,"td[contains(@class,'cdk-column-dateString')]/span").text

        # format date 
        dateString = datetime.strptime(url_date + dateString, "%Y-%m-%d%I:%M %p").strftime("%Y-%m-%d %H:%M:%S")

        temperature = tablerow.find_element(By.XPATH,"td[contains(@class,'cdk-column-temperature')]/lib-display-unit//span[@class='wu-value wu-value-to']").text
        dewPoint = tablerow.find_element(By.XPATH,"td[contains(@class,'cdk-column-dewPoint')]/lib-display-unit//span[@class='wu-value wu-value-to']").text
        humidity = tablerow.find_element(By.XPATH,"td[contains(@class,'cdk-column-humidity')]/lib-display-unit//span[@class='wu-value wu-value-to']").text
        windcardinal = tablerow.find_element(By.XPATH,"td[contains(@class,'cdk-column-windcardinal')]/span").text
        windSpeed = tablerow.find_element(By.XPATH,"td[contains(@class,'cdk-column-windSpeed')]/lib-display-unit//span[@class='wu-value wu-value-to']").text
        windGust = tablerow.find_element(By.XPATH,"td[contains(@class,'cdk-column-windGust')]/lib-display-unit//span[@class='wu-value wu-value-to']").text
        pressure = tablerow.find_element(By.XPATH,"td[contains(@class,'cdk-column-pressure')]/lib-display-unit//span[@class='wu-value wu-value-to']").text
        precipRate = tablerow.find_element(By.XPATH,"td[contains(@class,'cdk-column-precipRate')]/lib-display-unit//span[@class='wu-value wu-value-to']").text
        condition = tablerow.find_element(By.XPATH,"td[contains(@class,'cdk-column-condition')]/span").text
            
        entry = [dateString,temperature,dewPoint,humidity,windcardinal,windSpeed,windGust,pressure,precipRate,condition]
        data.append(entry);

    print("Done Table Crawl")

#main variables
data = []
url = "https://www.wunderground.com/history/daily/tr/seyhan/LTAF/date/2017-12-28"
curdate = datetime.strptime(url.split('/',10)[-1], "%Y-%m-%d")

#setup selenium
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
driver.get(url)

setupSite()

while True: 
    m = input("Mode? :")
    if m == "q":
        break;
    if m == "r":
        driver.refresh()
    if m == "n":
        nextDay()
    if m == "s":
        saveDataset(driver.current_url.split('/',10)[-3], data);
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