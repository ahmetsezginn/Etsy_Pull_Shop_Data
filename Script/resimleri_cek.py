
#resimleri_cek

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import re
import requests
def resimleri_indir_ve_kaydet(driver, url, hedef_klasor):

    # URL'den dosya adı temelini çıkarma
    dosya_temeli = re.search(r'/(\d+)/', url).group(1)

    # Resim elementlerini bul ve tekrarlanan linkleri önle
    WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img[data-src-zoom-image]")))
    resimler = driver.find_elements(By.CSS_SELECTOR, "img[data-src-zoom-image]")
    resim_url_listesi = []

    for resim in resimler:
        resim_url = resim.get_attribute("data-src-zoom-image")

        # Listede aynı URL var mı?
        if resim_url not in resim_url_listesi:
            resim_url_listesi.append(resim_url)

    # Resimleri indir ve kaydet
    for index, resim_url in enumerate(resim_url_listesi):
        resim_cevap = requests.get(resim_url)
        if resim_cevap.status_code == 200:
            resim_dosya_yolu = os.path.join(hedef_klasor, f"{dosya_temeli}_resim_{index + 1}.jpg")
            with open(resim_dosya_yolu, 'wb') as dosya:
                dosya.write(resim_cevap.content)
                
