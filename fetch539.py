import requests
from bs4 import BeautifulSoup

def fetch_539_latest_100():
    try:
        url = "https://2019.biga.com.tw/SERVICE/539%E9%96%8B%E7%8D%8E%E5%96%AE%E7%AC%AC1%E9%A0%81"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Referer": "https://2019.biga.com.tw/"
        }

        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        html = response.text

        # 儲存原始頁面方便 debug
        with open("debug.html", "w", encoding="utf-8") as debug_file:
            debug_file.write(html)

        soup = BeautifulSoup(html, "html.parser")
        rows = soup.find_all("tr")

        output_lines = []
        for row in rows:
            cols = row.find_all("div", class_="xno")
            if len(cols) == 8:
                date = cols[0].text.strip()
                weekday = cols[1].text.strip()
                draw = cols[2].text.strip()
                nums = [col.text.strip() for col in cols[3:]]
                line = f"{draw} {date} {weekday} {' '.join(nums)}"
                output_lines.append(line)

        if not output_lines:
            raise Exception("⚠️ 沒有抓到任何有效期數，可能是網站改版或被擋下來。")

        with open("last100.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(output_lines[:100]))

        print("[✅] 成功寫入 last100.txt，共", len(output_lines), "筆")
        
    except Exception as e:
        print(f"[❌] 發生錯誤: {e}")

if __name__ == "__main__":
    fetch_539_latest_100()
