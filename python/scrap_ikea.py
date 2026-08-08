from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv
from datetime import datetime
from time import sleep
import undetected_chromedriver as uc

"""opts = Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install()),
    options=opts
)"""
opts = uc.ChromeOptions()
driver = uc.Chrome(options=opts)


fecha = datetime.now().strftime("%d-%m-%Y")
tienda= "Ikea"

productos_csv = []

for pagina in range(1,4):
    url = f"https://www.ikea.com/cl/es/search/?q=macetero&page={pagina}"

    driver.get(url)
    sleep(6)

    cards = driver.find_elements(By.XPATH, "//div[contains(@class, 'plp-mastercard__price-components')]")

    for card in cards:

        try:
            nombre = card.find_element(By.XPATH, ".//span[contains(@class,'plp-price-module__description')]").text
        except:
            nombre= None

        try:
            marca= card.find_element(By.XPATH, ".//span[contains(@class, 'plp-price-module__product-name')]").text
        except:
            marca=None
        
        try:
            precio = card.find_element(By.XPATH, ".//span[contains(@class, 'plp-price__integer')]").text
            precio = int(precio.replace(".","").strip())
        except:
            precio = None

        productos_csv.append((nombre, marca, precio, tienda, fecha))

driver.quit()

with open(f"productos_ikea_{fecha}.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Producto","Marca", "Precio", "Tienda", "Fecha"])
    writer.writerows(productos_csv)