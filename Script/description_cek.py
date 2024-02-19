
#description_cek

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import re

# Açıklama Seçicisi
description_selector = "p[data-product-details-description-text-content]"

def aciklama_cek(driver, url, worksheet, row):
    description_selector = "p[data-product-details-description-text-content]"
    description = driver.find_element(By.CSS_SELECTOR, description_selector).text
    worksheet.cell(row=row, column=4, value=description)