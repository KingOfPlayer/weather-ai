from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.wunderground.com/history/daily/tr/seyhan/LTAF/date/2017-12-28")

while True: 
    m = input()
    if m == "q":
        break;
    if m == "r":
        driver.refresh();
    if m == "g":

        #cookies need accept

        tablebody = driver.find_element(By.XPATH,"//div[@class='observation-table ng-star-inserted']/table/tbody")
        tablerows = tablebody.find_elements(By.XPATH,"tr")
        for index, tablerow in enumerate(tablerows, start=1):
            entry = [];
            dateString = tablerow.find_element(By.XPATH,"td[contains(@class,'cdk-column-dateString')]/span").text
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
            
driver.close()