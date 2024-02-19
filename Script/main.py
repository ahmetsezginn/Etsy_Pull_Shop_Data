from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import os
import re
import title_cek
import hashtag_cek
import description_cek
import resimleri_cek
from linkleri_cek import kategori_ve_sayfalari_gez_ve_linkleri_cek

# Web sayfasını almak için Chrome seçenekleri
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

# Hedef Klasör
hedef_klasor = "C:\\Users\\MacTac\\Desktop\\siteden veri çekme\\hastag"
base_url = "https://www.etsy.com/shop/EmbroideryCoffeeShop?"
def dosya_adi_duzenle(adi):
    # Windows'ta geçersiz olan karakterleri çıkar
    adi = re.sub(r'[<>:"/\\|?*]', '', adi)
    return adi

def main():
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(base_url)
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".wt-tab__item[data-section-id]")))
        kategori_butonlari = driver.find_elements(By.CSS_SELECTOR, ".wt-tab__item[data-section-id]")
        
        kategori_bilgileri = {}
        for buton in kategori_butonlari:
            section_id = buton.get_attribute("data-section-id")
            kategori_adi = buton.find_element(By.CSS_SELECTOR, ".wt-break-word").text.strip()
            if section_id not in ["0", "1"]:
                kategori_bilgileri[section_id] = dosya_adi_duzenle(kategori_adi)
        # Her kategori için link listesi oluştur
        for section_id, kategori_adi in kategori_bilgileri.items():
            kategori_linkleri = kategori_ve_sayfalari_gez_ve_linkleri_cek(driver, base_url, section_id)
            kategori_klasoru = os.path.join(hedef_klasor, kategori_adi)
            os.makedirs(kategori_klasoru, exist_ok=True)
            kategori_dosya_yolu = os.path.join(kategori_klasoru, f"{kategori_adi}.txt")
            with open(kategori_dosya_yolu, 'w') as dosya:
                for link in kategori_linkleri:
                    dosya.write(link + "\n")

        # Her kategori için veri çekme işlemi
        for section_id, kategori_adi in kategori_bilgileri.items():
            kategori_klasoru = os.path.join(hedef_klasor, kategori_adi)
            kategori_dosya_yolu = os.path.join(kategori_klasoru, f"{kategori_adi}.txt")

            with open(kategori_dosya_yolu, 'r') as dosya:
                linkler = dosya.readlines()

            workbook = Workbook()
            worksheet = workbook.active
            satir_sayisi = 1

            for link in linkler:
                link = link.strip()
                basarili = False
                deneme_sayisi = 0

                while not basarili and deneme_sayisi < 3:  # Maksimum 3 deneme
                    try:
                        driver.execute_script("window.open(arguments[0]);", link)
                        driver.switch_to.window(driver.window_handles[1])

                        dosya_temeli = re.search(r'/(\d+)/', link).group(1)
                        worksheet.cell(row=satir_sayisi, column=1, value=dosya_temeli)
                        title_cek.title_cek(driver, link, worksheet, satir_sayisi)
                        hashtag_cek.hashtaglari_cek(driver, link, worksheet, satir_sayisi)
                        description_cek.aciklama_cek(driver, link, worksheet, satir_sayisi)
                        resimleri_cek.resimleri_indir_ve_kaydet(driver, link, kategori_klasoru)

                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        basarili = True
                    except Exception as e:
                        print(f"Hata: {e}. Link '{link}' için yeniden deneniyor...")
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        deneme_sayisi += 1

                satir_sayisi += 1

            workbook.save(os.path.join(kategori_klasoru, f"{kategori_adi}.xlsx"))

    except Exception as e:
        print("Büyük bir hata oluştu:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()