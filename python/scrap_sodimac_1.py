from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import datetime
import csv
import undetected_chromedriver as uc


opts = Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(
    service= Service(ChromeDriverManager().install()),
    options = opts
)

# trae 91 de 104 precios. los precios que no trae son porque el producto tiene +1 tamaño por ende +1 precio
"""opts = uc.ChromeOptions()
opts.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")"""

#driver = uc.Chrome(options=opts)

tienda = "Sodimac"
fecha = datetime.now().strftime("%d-%m-%Y")
productos_csv = []

for pagina in range(1, 8):  
    url = f"https://www.sodimac.cl/sodimac-cl/lista/CATG10520/Maceteros-y-Accesorios?page={pagina}&store=so_com"
    print("Scrapeando:", url)

    driver.get(url)
    sleep(5)

    cards = driver.find_elements(By.XPATH, "//div[contains(@class,'grid-pod')]")

    for card in cards:
        try:
            nombre = card.find_element(
                By.XPATH, ".//b[contains(@class,'pod-subTitle')]"
            ).text.strip()
        except:
            nombre = None

        try:
            marca = card.find_element(
                By.XPATH, ".//b[contains(@class,'pod-title')]"
            ).text.strip()
        except:
            marca = None

        try:
            precio = card.find_element(
                By.XPATH,
                ".//div[contains(@class, 'price')]//span"
            ).text.strip()
            precio = int(precio.replace("$","").replace(".","").strip())
        except:
            precio = None

        """try:
            link = card.find_element(
                By.XPATH, ".//a"
            ).get_attribute("href")
        except:
            link = None""" # LINK PRODUCTOS
        

        productos_csv.append((nombre,marca, precio, tienda, fecha))

driver.quit()


with open(f"productos_sodimac_{fecha}.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Producto","Marca","Precio","Tienda", "Fecha"])
    writer.writerows(productos_csv)

print("Total productos:", len(productos_csv))


