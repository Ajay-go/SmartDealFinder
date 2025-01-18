from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
options = Options()
driver = webdriver.Chrome(service= s, options= options)

####### getting prices at flipkart   ######
def scrape_prices_flipkart(detail):
   driver.get('https://www.flipkart.com/')
   time.sleep(2)
   input = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
   time.sleep(2)
   input.send_keys(detail)
   time.sleep(2)
   input.send_keys(Keys.ENTER)


   target_div = driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div')
   div_html = target_div.get_attribute('outerHTML')


   soup = BeautifulSoup(div_html, 'lxml')
   price_element = soup.find(class_='Nx9bqj _4b5DiR')
   price_text = price_element.text
   price_value = price_text.replace('₹', '').replace(',', '').strip()
   return price_value

######### getting prices at amazon ##############

def scrape_prices_amazon(detail):

   ## complete it
   return str(100)


# //*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]

# <div class="Nx9bqj _4b5DiR">₹35,780</div>
# <div class="Nx9bqj _4b5DiR">₹13,999</div>
