from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
s = Service(ChromeDriverManager().install())

from bs4 import BeautifulSoup

driver = webdriver.Chrome(service = s)

driver.get('https://www.cashify.in/sell-old-mobile-phone?__utmrg=BB_Search_Brand_021224_Central&utm_source=google&utm_medium=cpc&utm_campaign=BB_Search_Brand_021224_Central&utm_id=15069140359&utm_term=conversion&__utmrg=brand2c&utm_source=google&utm_medium=cpc&utm_campaign=BB_Search_Brand_021224_Central&utm_term=cashify&utm_content=555967663159&gad_source=1&gclid=CjwKCAiAhP67BhAVEiwA2E_9g6zOGKGAZOzAKTR67jlpw5b5XVpi1xkeoKjbnriMJAtuFzxLWDNSaBoCqNcQAvD_BwE')

time.sleep(2)
samsung = driver.find_element(by=By.XPATH,value='//*[@id="__csh"]/main/main/div/div[2]/div[1]/div[2]/div/section/div/div[1]/div[4]/div/div[2]/div[1]/div/a[3]/div/img')

samsung.click()
time.sleep(5)

height = driver.execute_script('return document.body.scrollHeight')
prevheight = height
    
while True:
   driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
   time.sleep(2)
   currheight = driver.execute_script('return document.body.scrollHeight')
        
   print(f"Previous Height: {prevheight}")
   print(f"Current Height: {currheight}")
        
   if currheight == prevheight:
      print("No more content to load.")
      break
        
   prevheight = currheight
   
time.sleep(10)

target_div = driver.find_element(By.XPATH, '/html/body/main/main/div/div[2]/div[2]/div[1]/div/div/div/div[4]')  
time.sleep(10)
div_html = target_div.get_attribute('outerHTML')

time.sleep(2)
with open('models.html', 'w', encoding='utf-8') as f:
    f.write(div_html)



from bs4 import BeautifulSoup

with open('models.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'lxml')

model_images = soup.find_all('img', alt=True)

model_names = [img['alt'] for img in model_images ]

for name in model_names:
    print(name)


