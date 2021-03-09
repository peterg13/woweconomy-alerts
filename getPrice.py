from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Firefox()
driver.get("https://theunderminejournal.com/#us/sargeras/item/171828")

try:
    #Gets the price of Laestrite Ore. Waits until page is loaded and the elements exist
    price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((by.By.CLASS_NAME, "current-price")))
    currentPrice = price.find_element(by.By.CLASS_NAME, "money-gold").text

    #Gets the last updated time and the next update time
    updateTimes = driver.find_element_by_id("realm-updated").find_elements_by_class_name("full-date")
    lastUpdated = updateTimes[0].get_attribute("title")
    nextUpdate = updateTimes[1].get_attribute("title")
    
    #this value gets returned to the main process which will be used to determine the price and next time to scan
    returnValue = {"current_price" : currentPrice, "last_updated" : lastUpdated, "next_update" : nextUpdate}
    print(returnValue)


    
finally:
    driver.close()