
#title_cek

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def title_cek(driver, url, worksheet, row):
    xpath = "//div[@class='wt-mb-xs-1']/h1"

    # Belirtilen XPath'e sahip elementin yüklenmesini bekle
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        title = driver.find_element(By.XPATH, xpath).text
        worksheet.cell(row=row, column=2, value=title)
    except Exception as e:
        print(f"Hata: Başlık için '{url}' sayfasında belirtilen XPath '{xpath}' bulunamadı. Hata mesajı: {e}")