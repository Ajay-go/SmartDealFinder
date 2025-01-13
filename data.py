from bs4 import BeautifulSoup

with open('models.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'lxml')

model_images = soup.find_all('img', alt=True)

model_names = [img['alt'] for img in model_images ]

samsung_dict  = {'samsung' :[]}
for name in model_names:
    samsung_dict['samsung'].append(name)

print(samsung_dict)


############################################################################

from bs4 import BeautifulSoup

with open('model.html','r', encoding='utf-8') as file:
    html_content = file.read()
    
soup = BeautifulSoup(html_content,'lxml')

# container = soup.find_all('div',{'class':'w-1/3 sm:w-auto sm:col-span-1 h-auto sm:max-h-56 sm:rounded-lg border-b border-r border-gray-200 border-solid sm:shadow-md flex flex-col'})

# for i in container:
#     print(i.find("title"))

model_images = soup.find_all('img',alt=True)

model_names = [img['alt'] for img in model_images]  

apple_dict = {'apple' : []}
for name in model_names:
    apple_dict['apple'].append(name)
    
print(apple_dict)    

import pandas as pd 
df=pd.DataFrame({
    'model':apple_dict
})

print(df.head())
    