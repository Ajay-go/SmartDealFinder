from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

s = Service(ChromeDriverManager().install())
options = Options()
driver = webdriver.Chrome(service= s, options= options)

def scrape_samsung():
    driver.get('https://www.cashify.in/sell-old-mobile-phone')
    time.sleep(2)
    samsung = driver.find_element(by=By.XPATH, value='//*[@id="__csh"]/main/main/div/div[2]/div[1]/div[2]/div/section/div/div[1]/div[4]/div/div[2]/div[1]/div/a[3]/div/img')
    samsung.click()
    time.sleep(5)

    # Scroll to load all content
    prevheight = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)
        currheight = driver.execute_script('return document.body.scrollHeight')
        if currheight == prevheight:
            break
        prevheight = currheight

    time.sleep(5)

    # Extract the phone model data from the loaded page
    target_div = driver.find_element(By.XPATH, '/html/body/main/main/div/div[2]/div[2]/div[1]/div/div/div/div[4]')
    div_html = target_div.get_attribute('outerHTML')
    with open('samsung_models.html', 'w', encoding='utf-8') as f:
        f.write(div_html)

    with open('samsung_models.html', 'r', encoding='utf-8') as file:
        html_content = file.read()



# Function to scrape Apple phone data
def scrape_apple():
    driver.get('https://www.cashify.in/buy-sell-used-mobile-phones')
    time.sleep(2)
    apple = driver.find_element(by=By.XPATH, value='//*[@id="__csh"]/main/main/div/div/div/div[2]/div[3]/div/section/div/div[1]/div[4]/div/div[2]/div[1]/div/a[1]')
    apple.click()
    time.sleep(5)

    # Scroll to load all content
    prevheight = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        currheight = driver.execute_script('return document.body.scrollHeight')
        if currheight == prevheight:
            break
        prevheight = currheight

    time.sleep(5)

    # Extract the phone model data from the loaded page
    target_div = driver.find_element(by=By.XPATH, value='//*[@id="__csh"]/main/main/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div')
    div_html = target_div.get_attribute('outerHTML')
    with open('apple_models.html', 'w', encoding='utf-8') as f:
        f.write(div_html)

    


# Scrape both Apple and Samsung data
samsung_data = scrape_samsung()
apple_data = scrape_apple()
def scrape_oneplus() :
    driver.get('https://www.cashify.in/sell-old-mobile-phone/sell-oneplus')
    
    web_page = driver.page_source
    
    with open('oneplus_models.html', 'w', encoding= 'utf-8') as f :
        f.write(web_page)
    
scrape_oneplus()
