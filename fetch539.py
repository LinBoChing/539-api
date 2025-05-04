import requests
from bs4 import BeautifulSoup

def fetch_539_latest_100():
    try:
        url = "https://2019.biga.com.tw/SERVICE/539%E9%96%8B%E7%8D%8E%E5%96%AE%E7%AC%AC1%E9%A0%81"
        response = requests.get(url)
        response.encoding = "utf-8"

        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.select("tr")

        result = []
        for row in rows:
            cols = row.find_all("div", class_="xno")
            if len(cols) == 8:
                date = cols[0].text.strip()
                week = cols[1].text.strip()
                round_no = cols[2].text.strip()
                numbers = [c.text.strip().zfill(2) for c in cols[3:]]
                result.append(f"{round_no} {date} {week} {' '.join(numbers)}")

        with open("last100.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(result[:100]))

        print("[✅] 成功寫入 last100.txt")

    except Exception as e:
        print(f"[❌] 錯誤：{e}")

if __name__ == "__main__":
    fetch_539_latest_100()
