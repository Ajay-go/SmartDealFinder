import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Selenium WebDriver setup for Chrome
options = Options()
options.add_argument("--headless")  # Runs the browser in the background
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)

# Function to scrape Samsung phone data
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

    soup = BeautifulSoup(html_content, 'lxml')
    samsung_models = [img['alt'] for img in soup.find_all('img', alt=True)]
    
    return {'Samsung': samsung_models}

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

    with open('apple_models.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'lxml')
    apple_models = [img['alt'] for img in soup.find_all('img', alt=True)]
    
    return {'Apple': apple_models}

# Scrape both Apple and Samsung data
samsung_data = scrape_samsung()
apple_data = scrape_apple()

# Combine both Samsung and Apple data
combined_data = {**samsung_data, **apple_data}

# Function to filter data based on user input
def filter_phones(brand, model, ram, rom, color):
    # Mock filtering function
    return [f"{brand} {model} - {ram}GB RAM, {rom}GB ROM, {color} color"]

# Streamlit UI
st.title("Smart Deal Finder")

# Dropdown for selecting brand
brands = list(combined_data.keys())
selected_brand = st.selectbox("Select Brand", brands)

# Dropdown for selecting model based on the selected brand
selected_model = st.selectbox("Select Model", combined_data[selected_brand])

# Dropdown for RAM
ram_options = [4, 6, 8, 12]  # Modify based on your data
selected_ram = st.selectbox("Select RAM", ram_options)

# Dropdown for ROM
rom_options = [64, 128, 256, 512]  # Modify based on your data
selected_rom = st.selectbox("Select ROM", rom_options)

# Dropdown for color
color_options = ["Black", "White", "Blue", "Red"]  # Modify based on your data
selected_color = st.selectbox("Select Color", color_options)

# Button to show filtered result
if st.button("Find Deals"):
    filtered_phones = filter_phones(selected_brand, selected_model, selected_ram, selected_rom, selected_color)
    
    # Display the filtered phones
    st.write("Available Phones:")
    for phone in filtered_phones:
        st.write(phone)

# Cleanup: Close the Selenium WebDriver
driver.quit()
