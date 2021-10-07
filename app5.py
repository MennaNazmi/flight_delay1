import selenium
selenium.__file__
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


PATH="C:\\Users\\Menna Nazmi\\Downloads\\chromedriver_win32\\chromedriver.exe"

driver= webdriver.Chrome(PATH)

driver.get ("https://www.flightstats.com/v2/flight-tracker/departures/CAI")


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "pagination__PageNavItem-sc-1515b5x-2 fOBbUj"))
    )
finally:
   driver.quit()



#link=driver.find_element_by_class_name("pagination__PageNavigation-sc-1515b5x-3 bFumhV")
#link.click()

#element=WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH ,"//a[@class=pagination__PageNavigation-sc-1515b5x-3 bFumhV']")))
#element.click()