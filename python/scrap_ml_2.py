from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import datetime
import csv
import pandas as pd
import undetected_chromedriver as uc

opts = Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

"""opts= uc.ChromeOptions()
driver= uc.Chrome(options=opts)"""

fecha = datetime.now().strftime("%d-%m-%Y")
tienda = "Mercado Libre"
productos_csv = []

for pagina in range(1, 2):  # 5 trae 197 productos
    base = "https://listado.mercadolibre.cl/hogar-muebles/jardin-aire-libre/decoracion-exterior/macetas-maceteros/nuevo"
    desde = pagina * 48 + 1
    if pagina == 0:
        url = f"{base}/maceteros_NoIndex_True?sb=all_mercadolibre"
    else:
        url = f"{base}/maceteros_Desde_{desde}_NoIndex_True?sb=all_mercadolibre"

    driver.get(url)
    sleep(5)

    cards = driver.find_elements(By.XPATH, "//div[contains(@class,'poly-card')]")

    for card in cards:
        try:
            nombre = card.find_element(
                By.XPATH, ".//a[contains(@class,'poly-component__title')]"
            ).text.strip()
        except:
            nombre = None

        try:
            precio = card.find_element(
                By.XPATH,
                ".//div[contains(@class,'poly-price__current')]//span[contains(@class,'andes-money-amount__fraction')]"
            ).text.strip()
            precio = int(precio.replace(".", ""))
        except:
            precio = None

        try:
            link = card.find_element(
                By.XPATH, ".//a[contains(@class,'poly-component__title')]"
            ).get_attribute("href")
        except:
            link = None
        
        productos_csv.append((nombre, precio, tienda, fecha, link))

driver.quit()

productos_csv = list(set(productos_csv)) # sin duplicados
with open(f"productos_ml_{fecha}.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Producto", "Precio", "Tienda", "Fecha"])
    writer.writerows(productos_csv)

print("Total productos:", len(productos_csv))
