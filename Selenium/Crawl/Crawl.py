from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
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
        table = driver.find_elements(By.XPATH, "//table[@class='mat-table cdk-table mat-sort ng-star-inserted']/tbody[@role='rowgroup']/tr")
        for row in table:
            cols = row.find_elements(By.XPATH, "//span[@class='wu-value wu-value-to'][1]")
            for col in cols:
                print(col.text)
        
driver.close()