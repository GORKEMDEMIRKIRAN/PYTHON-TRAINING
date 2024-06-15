
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import TimeoutException,WebDriverException,NoSuchElementException

from selenium.webdriver.edge.service import Service as sv_edge


import time

url="https://eksisozluk.com"
url1="https://www.google.com/maps"

servic_edge=sv_edge(".\\24-selenium_eksi_sözlük\\msedgedriver.exe")
driver_edge=webdriver.Edge(service=servic_edge)
driver_edge.get(url)

elements=driver_edge.find_element(By.CSS_SELECTOR,id="content")
for element in elements:
    print(element.text)

time.sleep(40)
# driver_edge.close()





