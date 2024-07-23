import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service

chromedriver = r'C:\Users\kmontero\chromedriver_win32\chromedriver.exe'
url = 'https://glossary.istqb.org/en_US/search?term=&exact_matches_first=true&page=49'

service = Service(chromedriver)
driver = webdriver.Chrome(service=service)
driver.get(url)

WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME, 'cc-nb-okagree')))
driver.find_element(By.CLASS_NAME, 'cc-nb-okagree').click()
time.sleep(5)

text = ''
for i in range(567):
    word = driver.find_elements(By.TAG_NAME, 'h3')[i].text
    definition = driver.find_elements(By.TAG_NAME, 'p')[i+3].text
    text += word + '\n' + definition + '\n' + '\n'

# this is sample change

with open('ISTQB Glossary.txt', 'w') as file:
    file.write(text)
