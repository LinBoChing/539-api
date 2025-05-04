import requests
from bs4 import BeautifulSoup

url = "https://2019.biga.com.tw/SERVICE/539%E9%96%8B%E7%8D%8E%E5%96%AE%E7%AC%AC1%E9%A0%81"
res = requests.get(url)
res.encoding = "utf-8"

soup = BeautifulSoup(res.text, "html.parser")
rows = soup.find_all("tr")

results = []
for row in rows:
    cols = row.find_all("div", class_=["f12", "xno"])
    if len(cols) == 8:
        _, week, period, n1, n2, n3, n4, n5 = [c.text.strip() for c in cols]
        results.append(f"{period},{n1},{n2},{n3},{n4},{n5}")

with open("last100.txt", "w", encoding="utf-8") as f:
    for line in results[:100]:
        f.write(line + "\n")
