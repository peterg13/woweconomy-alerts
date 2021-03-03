from selenium import webdriver
from webdriverPath import firefoxDriverPath


driver = webdriver.Firefox(executable_path = firefoxDriverPath)
driver.get("https://youtube.com")
driver.close()