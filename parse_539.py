from bs4 import BeautifulSoup
import re

with open('debug.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

data = []

trs = soup.find_all('tr')[1:]

for tr in trs:
    tds = tr.find_all('td')
    if len(tds) != 12:
        continue

    for i in [0, 6]:
        period = tds[i].text.strip()
        date_raw = tds[i+1].text.strip()
        weekday = tds[i+2].text.strip()
        numbers = [tds[i+3].text.strip(), tds[i+4].text.strip(), tds[i+5].text.strip(), tds[i+6].text.strip(), tds[i+7].text.strip()]

        match = re.search(r'(\d{4})年(\d{2})月(\d{2})日', date_raw)
        if match:
            formatted_date = f"{match.group(1)}/{match.group(2)}/{match.group(3)}"
        else:
            continue

        line = f"{period},{formatted_date},{weekday}," + ",".join(numbers)
        data.append(line)

data = data[:100]

with open('last100.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(data))

print("✅ 擷取完成，已寫入 last100.txt，共", len(data), "筆資料")
