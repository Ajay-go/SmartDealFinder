from bs4 import BeautifulSoup

with open('C:/Users/ajayg/OneDrive/Desktop/pro2/SmartDealFinder/models.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'lxml')

model_images = soup.find_all('img', alt=True)

model_names = [img['alt'] for img in model_images ]

samsung_dict  = {'samsung' :[]}
for name in model_names:
    samsung_dict['samsung'].append(name)

print(samsung_dict)

print()

############################################################################

from bs4 import BeautifulSoup

with open('SmartDealFinder/apple_models.html','r', encoding='utf-8') as file:
    html_content = file.read()
    
soup = BeautifulSoup(html_content,'lxml')



model_images = soup.find_all('img',alt=True)

model_names = [img['alt'] for img in model_images]  

apple_dict = {'apple' : []}
for name in model_names:
    apple_dict['apple'].append(name)
    
print(apple_dict)    

print()

oneplus_list = []

with open('SmartDealFinder/oneplus_models.html','r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'lxml')

for i in soup.find_all('div', class_ = 'flex flex-col items-center justify-center cursor-pointer w-full h-full bg-primary-bg p-2 sm:p-4 sm:min-w-full rounded-0 sm:rounded-xl sm:shadow-md sm:max-h-56 sm:max-w-40') :

    oneplus_list.append(i.find('span', class_ = 'caption text-center line-clamp-3').text.strip())


print(oneplus_list)    
    