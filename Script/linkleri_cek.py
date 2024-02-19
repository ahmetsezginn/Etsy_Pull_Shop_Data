from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Kategori ve sayfaları gezerek linkleri çekme fonksiyonu
def kategori_ve_sayfalari_gez_ve_linkleri_cek(driver, base_url, section_id):
    sayfa_numarasi = 1
    kategori_linkleri = []

    while True:
        guncel_sayfa_url = f"{base_url}section_id={section_id}&page={sayfa_numarasi}"
        driver.get(guncel_sayfa_url)

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".responsive-listing-grid.wt-grid.wt-grid--block.wt-justify-content-flex-start.wt-mb-xs-3.appears-ready")))
            kategori_linkleri.extend(linkleri_cek(driver))
            sayfa_numarasi += 1
        except TimeoutException:
            break

    return kategori_linkleri

# Bulunan linkleri çekme fonksiyonu
def linkleri_cek(driver):
    elementler = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".responsive-listing-grid.wt-grid.wt-grid--block.wt-justify-content-flex-start.wt-mb-xs-3.appears-ready a")))
    return [element.get_attribute('href') for element in elementler]
