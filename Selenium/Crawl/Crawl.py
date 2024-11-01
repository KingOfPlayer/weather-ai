from telnetlib import DO
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.wunderground.com/history/daily/tr/seyhan/LTAF/date/2017-12-28")

driver.refresh()
while True: 
    m = input()
    if m == "q":
        break;
    if m == "r":
        driver.refresh();
    if m == "g":
        ## mat-table cdk-table mat-sort ng-star-inserted
        table = driver.find_element(By.CLASS_NAME,"mat-table cdk-table mat-sort ng-star-inserted")
        print(table.text)
        

driver.close()