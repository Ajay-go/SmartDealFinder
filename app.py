from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

s = Service(ChromeDriverManager().install())
options = Options()
driver = webdriver.Chrome(service= s, options= options)

def scrape_oneplus() :
    driver.get('https://www.cashify.in/sell-old-mobile-phone/sell-oneplus')
    
    name = []

    web_page = driver.page_source
    
    with open('oneplus_models.html', 'w', encoding= 'utf-8') as f :
        f.write(web_page)
    
    soup = BeautifulSoup(web_page, 'lxml')

    for i in soup.find_all('div', class_ = 'flex flex-col items-center justify-center cursor-pointer w-full h-full bg-primary-bg p-2 sm:p-4 sm:min-w-full rounded-0 sm:rounded-xl sm:shadow-md sm:max-h-56 sm:max-w-40') :

        name.append(i.find('span', class_ = 'caption text-center line-clamp-3').text.strip())
        
    return {'Oneplus' : name}
        
        
oneplus_data = scrape_oneplus()
