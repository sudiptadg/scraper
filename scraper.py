
from flask import Flask, Response
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import datetime
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

app = Flask(__name__)


@app.route('/')
def hello_world(): 
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
    header=""
    for cell in cells:
        header = header + cell.string + ','
    
    header = header + "\n"

    for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            header = header + cell.string + ','

        header = header + "\n"
    
    browser.quit()
    headers = "attachment; filename=" + datetime.datetime.now().strftime('%Y_%m_%d %H_%M_%S') + ".csv"
    return Response(
        header,
        mimetype="text/csv",
        headers={"Content-disposition": headers})

if __name__ == '__main__':
    app.run(host='0.0.0.0')





