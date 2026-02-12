import requests
from bs4 import BeautifulSoup
import os

def kontrol_et():
    url = "https://www.amazon.com.tr/gp/aw/d/B0CFW1CWHW/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=459dadc67547fabb460bca53d8699072&hsa_cr_id=0&qid=1770909037&sr=1-3-e0fa1fdd-d857-4087-adda-5bd576b25987&aref=mda3d1lXaZ&ref_=sbx_s_sparkle_sbtcd_asin_2_img&pd_rd_w=NJnYO&content-id=amzn1.sym.498e0fe4-f72f-4080-a630-1c61e22377dd%3Aamzn1.sym.498e0fe4-f72f-4080-a630-1c61e22377dd&pf_rd_p=498e0fe4-f72f-4080-a630-1c61e22377dd&pf_rd_r=P4CHWWEDPFNJTHN12FE4&pd_rd_wg=8VxbA&pd_rd_r=528e3626-2b24-4ce3-bfe5-3c03ec6bb5f2" # Takip linkin
    hedef_fiyat = 1.098 # Hedeflediğin fiyat
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
