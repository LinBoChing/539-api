import requests
from bs4 import BeautifulSoup

def fetch_539_latest_100():
    try:
        url = "https://2019.biga.com.tw/SERVICE/539%E9%96%8B%E7%8D%8E%E5%96%AE%E7%AC%AC1%E9%A0%81"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'

        # 寫出 debug 用的 HTML，方便你排查
        with open("debug.html", "w", encoding="utf-8") as f:
            f.write(response.text)

        soup = BeautifulSoup(response.text, "html.parser")
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

        if not output_lines:
            print("❌ 沒有抓到任何有效的資料，可能是網站格式改變或被擋。")
        else:
            output = "\n".join(output_lines[:100])
            with open("last100.txt", "w", encoding="utf-8") as f:
                f.write(output)
            print(f"✅ 成功寫入 {len(output_lines[:100])} 筆資料到 last100.txt")

    except Exception as e:
        print(f"[❌] 發生錯誤：{e}")

if __name__ == "__main__":
    fetch_539_latest_100()
