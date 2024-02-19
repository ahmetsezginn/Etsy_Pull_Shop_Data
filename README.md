# Etsy_Pull_Shop_Data
Proje etsy de var olan bir dükkanın başka bir websitesine geçerken arşivi olmadığı için geçmelerine yardımcı olan bir projedir.
Programın çalışması için gerekenler: Etsy de var olan bir mağaza linki ve bilgisayarınızda var olan bir klasör uzantısı.
Programın sahip olduğu kütüphaneler. selenium kütüphanesinden: webdriver,By,WebDriverWait,expected_conditions, TimeoutException kütüphanelerini kullanmaktadır.Program openpyxl kütüphanesinden: Workbook kütüphanesini kullanmaktadır. Program temel kütüphanelerden os, re, requests kütüphanelerini kullanmaktadır.
Kütüphanelerin kullanım amaçları:
  selenium:
    webdriver: Web tarayıcılarını otomatik olarak kontrol etmek için kullanılır.
    By: HTML öğelerini belirli seçicilere göre bulmak için kullanılır.
    WebDriverWait: Belirli bir koşul gerçekleşene kadar beklemek için kullanılır.
    expected_conditions: Belirli bir koşulun gerçekleşip gerçekleşmediğini kontrol etmek için kullanılır.
    TimeoutException: Belirlenen süre içinde bir koşulun gerçekleşmemesi durumunda hata fırlatmak için kullanılır.
  openpyxl:
    Workbook: Excel dosyaları oluşturmak ve düzenlemek için kullanılır.
  Temel kütüphaneler:
    os: İşletim sistemiyle ilgili işlevleri gerçekleştirmek için kullanılır.
    re: Düzenli ifadelerle (regex) çalışmak için kullanılır.
    requests: HTTP istekleri göndermek için kullanılır.
Programın çalışması için selenium kütüphanesini ve openpyxl kütüphanesi yüklemeniz yeterli olacaktır.
  Selenium Kütüphanesini Yüklemek İçin:
    pip install selenium
  Openpyxl Kütüphanesini Yüklemek İçin:
    pip install openpyxl
