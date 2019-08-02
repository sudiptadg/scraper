
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")

url = "http://95.216.2.220/com/24rate/rtncv2.html"
browser = webdriver.Chrome(executable_path = os.path.abspath('chromedriver'), chrome_options=chrome_options)
browser.implicitly_wait(10)
browser.get(url)

myDynamicElement = browser.find_element_by_class_name("bg-info")
html = browser.page_source
  
soup = BeautifulSoup(html, 'html5lib') 
table = soup.find(id="datatable3")

rows = table.findChildren(['tr'])

row = rows[0]
cells = row.findChildren('th')
print()
for cell in cells:
    print(cell.string, end=",") 

for row in rows:
    cells = row.findChildren('td')
    print()
    for cell in cells:
        print(cell.string, end=",")

browser.quit()