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