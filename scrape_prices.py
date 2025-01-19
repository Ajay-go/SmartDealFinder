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

    driver.get('https://www.amazon.in/')
    
    try : # if captcha doesn't comes
        amazon_search_box = driver.find_element('xpath', value= '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/div/input')
        amazon_search_box.send_keys(detail)

        time.sleep(2)

        amazon_search_box.send_keys(Keys.ENTER)
        time.sleep(5)
        web_page = driver.page_source
        
        soup = BeautifulSoup(web_page, 'lxml')

        price = "10"
        for i in soup.find_all('div', class_ = 'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16') : # if items comes in row wise fashion
            price = i.find('span', class_ = 'a-offscreen').text.strip()
            break
            
        if price == '10' : # if items comes in column wise fashion
            for i in soup.find_all('div', class_ = 'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20') :
                price = i.find('span', class_ = 'a-offscreen').text.strip()
                break
            
        time.sleep(5)
        return price[1 :].replace(',', '')

    except : # if captcha comes
        
        from amazoncaptcha import AmazonCaptcha
        
        link = driver.find_element('xpath', value= '/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/img').get_attribute('src')
        
        captcha = AmazonCaptcha.fromlink(link)
        
        ans = AmazonCaptcha.solve(captcha)
        
        input = driver.find_element('xpath', value= '/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[2]/input')
        input.send_keys(ans)
        time.sleep(2)
        input.send_keys(Keys.ENTER)
        
        amazon_search_box = driver.find_element('xpath', value= '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/div/input')
        amazon_search_box.send_keys(detail)

        time.sleep(2)

        amazon_search_box.send_keys(Keys.ENTER)

        time.sleep(5)
        web_page = driver.page_source
            
        soup = BeautifulSoup(web_page, 'lxml')

        price = "10"
        for i in soup.find_all('div', class_ = 'sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16') : # if items comes in row wise fashion
            price = i.find('span', class_ = 'a-offscreen').text.strip()
            break
        
        if price == '10' : # if items comes in column wise fashion
            for i in soup.find_all('div', class_ = 'sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20') :
                price = i.find('span', class_ = 'a-offscreen').text.strip()
                break
        
        time.sleep(5)
        return price[1 :].replace(',', '')
