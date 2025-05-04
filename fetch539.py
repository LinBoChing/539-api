import requests
from bs4 import BeautifulSoup
import os

def fetch_539_latest_100():
    try:
        # ⚠️ 切換當前目錄為 fetch539.py 所在位置
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        url = "https://2019.biga.com.tw/SERVICE/539%E9%96%8B%E7%8D%8E%E5%96%AE%E7%AC%AC1%E9%A0%81"
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, "html.parser")

        print("[🧪] Preview HTML:", response.text[:1000])  # debug

        rows = soup.find_all("tr")
        output_lines = []

        for row in rows:
            cols = row.find_all("div", class_="xno")
            if len(cols) == 8:
                date = cols[0].text.strip()
                weekday = cols[1].text.strip()
                draw = cols[2].text.strip()
                nums = [col.text.strip() for col in cols[3:]]
                output_lines.append(f"{draw} {date} {weekday} {' '.join(nums)}")

        output = "\n".join(output_lines[:100])
        with open("last100.txt", "w", encoding="utf-8") as f:
            f.write(output)

        print(f"[✅] 成功寫入 {len(output_lines)} 筆資料到 last100.txt")

    except Exception as e:
        print(f"[❌] 發生錯誤：{e}")

if __name__ == "__main__":
    fetch_539_latest_100()
