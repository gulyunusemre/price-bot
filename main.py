import requests
from bs4 import BeautifulSoup
import os

def kontrol_et():
    url = "https://www.amazon.com.tr/dp/B0BBRZ96S1" # Takip linkin
    hedef_fiyat = 600 # Hedeflediğin fiyat
    headers = {"User-Agent": "Mozilla/5.0"}
    
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")
    
    try:
        fiyat_metni = soup.find("span", {"class": "a-price-whole"}).text
        guncel_fiyat = int(fiyat_metni.replace(".", "").replace(",", ""))
        
        if guncel_fiyat <= hedef_fiyat:
            token = os.getenv("TELEGRAM_TOKEN")
            chat_id = os.getenv("CHAT_ID")
            mesaj = f"LEGO İNDİRİMİ! Fiyat: {guncel_fiyat} TL. Link: {url}"
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={mesaj}")
    except:
        print("Hata oluştu.")

if __name__ == "__main__":
    kontrol_et()
