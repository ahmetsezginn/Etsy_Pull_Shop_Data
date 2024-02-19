
#hashtag_cek

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import re
# CSS Seçiciler
css_selector1 = "li.wt-display-flex-xs h3.tag-card-title"
css_selector2 = "li.wt-action-group__item-container a.wt-btn"

def hashtaglari_cek(driver, url, worksheet, row):
    dosya_adi = re.search(r'/(\d+)/', url).group(1)
    hashtagler = []

    # İlk CSS seçicisi için metinleri deneme
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector1)))
        elementler1 = driver.find_elements(By.CSS_SELECTOR, css_selector1)
        hashtagler.extend([eleman.text for eleman in elementler1 if eleman.text])
    except Exception as e:
        print(f"CSS seçicisi {css_selector1} için element bulunamadı: {e}")

    # İkinci CSS seçicisi için metinleri deneme
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector2)))
        elementler2 = driver.find_elements(By.CSS_SELECTOR, css_selector2)
        hashtagler.extend([eleman.text for eleman in elementler2 if eleman.text])
    except Exception as e:
        print(f"CSS seçicisi {css_selector2} için element bulunamadı: {e}")

    # Filtrelenmiş hashtag'leri birleştir
    temiz_hashtagler = [ht for ht in hashtagler if not re.search(r'(Current page|Previous page|Next page|Page \d+|\A\d+\Z)', ht)]

    # Excel dosyasına yaz
    worksheet.cell(row=row, column=3, value=', '.join(temiz_hashtagler))