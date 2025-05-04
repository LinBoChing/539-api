import requests
from bs4 import BeautifulSoup

def fetch_539_latest_100():
    try:
        url = "https://www.pilio.idv.tw/lto539/listbbk.asp"
        response = requests.get(url)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")

        table = soup.find("table")
        rows = table.find_all("tr")[1:]  # skip header row
        result = []

        for row in rows[:100]:  # 最多抓100期
            cols = row.find_all("td")
            if len(cols) >= 9:
                draw = cols[0].text.strip()
                date = cols[1].text.strip()
                week = cols[2].text.strip()
                numbers = [cols[i].text.strip().zfill(2) for i in range(3, 8)]
                result.append(f"{draw} {date} {week} {' '.join(numbers)}")

        with open("last100.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(result))

        print("[✅] 已成功寫入 last100.txt")

    except Exception as e:
        print(f"[❌] 發生錯誤: {e}")

if __name__ == "__main__":
    fetch_539_latest_100()
