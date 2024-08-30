
from bs4 import BeautifulSoup

FILE_NAME = '1.html'
DATA_SELECTOR = '#video-title'




with open(FILE_NAME, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
data_elements = soup.select(DATA_SELECTOR)
data_list = [element.text.strip() for element in data_elements]

seen_starts = set()

filtered = []
for item in data_list:
    start = item[:30]
    if start not in seen_starts:
        filtered.append(item)
        seen_starts.add(start)

for i in range(len(filtered)):
    filtered[i] = filtered[i][:filtered[i].find('Warhammer40000')-3]


for item in filtered:
    columns = item.split(' | ')
    print(' \t| '.join(columns))

print(len(filtered))