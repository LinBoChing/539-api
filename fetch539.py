import requests
from bs4 import BeautifulSoup
import os

def fetch_539_latest_100():
    try:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        url = "https://2019.biga.com.tw/SERVICE/539%E9%96%8B%E7%8D%8E%E5%96%AE%E7%AC%AC1%E9%A0%81"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.find("table")
        rows = table.find_all("tr")
        output_lines = []

        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 6:
                draw = cols[0].text.strip()
                date = cols[1].text.strip()
                weekday = cols[2].text.strip()
                numbers = cols[3].text.strip().split()
                if len(numbers) == 5:
                    nums_formatted = ' '.join(n.zfill(2) for n in numbers)
                    output_lines.append(f"{draw} {date} {weekday} {nums_formatted}")

        with open("last100.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(output_lines[:100]))

        print(f"[✅] 成功寫入 {len(output_lines)} 筆資料到 last100.txt")

    except Exception as e:
        print(f"[❌] 發生錯誤：{e}")

if __name__ == "__main__":
    fetch_539_latest_100()
