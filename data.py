from bs4 import BeautifulSoup

with open('C:/Users/ajayg/OneDrive/Desktop/pro2/SmartDealFinder/models.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'lxml')

model_images = soup.find_all('img', alt=True)

model_names = [img['alt'] for img in model_images ]

samsung_list = []
for name in model_names:
    samsung_list.append(name)

# print(samsung_list)

# print()

############################################################################

from bs4 import BeautifulSoup

with open('C:/Users/ajayg/OneDrive/Desktop/pro2/SmartDealFinder/apple_models.html','r', encoding='utf-8') as file:
    html_content = file.read()
    
soup = BeautifulSoup(html_content,'lxml')



model_images = soup.find_all('img',alt=True)

model_names = [img['alt'] for img in model_images]  

apple_list = []
for name in model_names:
    apple_list.append(name)
    
# print(apple_list)    

print()

########################################################################
oneplus_list = []

with open('C:/Users/ajayg/OneDrive/Desktop/pro2/SmartDealFinder/oneplus_models.html','r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'lxml')

for i in soup.find_all('div', class_ = 'flex flex-col items-center justify-center cursor-pointer w-full h-full bg-primary-bg p-2 sm:p-4 sm:min-w-full rounded-0 sm:rounded-xl sm:shadow-md sm:max-h-56 sm:max-w-40') :

    oneplus_list.append(i.find('span', class_ = 'caption text-center line-clamp-3').text.strip())


# print(oneplus_list)    


#########################################################

import streamlit as st 
All_data = {
    'samsung': samsung_list,
    'apple': apple_list,
    'oneplus': oneplus_list
}

st.title("Smart Deal Finder")

# Dropdown for selecting brand
brands = ['samsung', 'apple', 'oneplus']
selected_brand = st.selectbox("Select Brand", brands)

# Dropdown for selecting model based on the selected brand
selected_model = st.selectbox("Select Model", All_data[selected_brand])

# Dropdown for RAM
ram_options = [4, 6, 8, 12]
selected_ram = st.selectbox("Select RAM", ram_options)

# Dropdown for ROM
rom_options = [64, 128, 256, 512]  # Modify based on your data
selected_rom = st.selectbox("Select ROM", rom_options)

butt = st.button('find prices')

if(butt):
    # price_at_flipkart = scrape_prices_flipkart()
    # price_at_amazon = scrape_prices_amazon()

    col1,col2 = st.columns(2)

    with col1:
        st.subheader("price at flipkart {}".format(100))
    with col2:
        st.subheader("price at amazon {}".format(1000))

