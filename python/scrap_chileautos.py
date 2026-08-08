from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from time import sleep
import csv
import undetected_chromedriver as uc

opts = uc.ChromeOptions()
opts.add_argument(r"--user-data-dir=C:\Users\Felipe\AppData\Local\Google\Chrome\User Data") 
opts.add_argument("--profile-directory=Profile 1")
opts.add_argument("--disable-blink-features=AutomationControlled")
opts.add_argument("--no-first-run")
opts.add_argument("--no-default-browser-check")
opts.add_argument("--start-maximized")

driver = uc.Chrome(options=opts)

tienda = 'Chileautos'
fecha = datetime.now().strftime('%d-%m-%Y')
productos_csv = []

for pagina in range(0,2):
    base = f'https://www.chileautos.cl/vehiculos/usado-tipo'

    if pagina == 0:
        url = base
    else:
        pagina = pagina * 12
        url = f"{base}/?offset={pagina}"

    driver.get(url)
    sleep(30)

    cards = driver.find_elements(By.XPATH,"//div[contains(@class, 'listing-item')]")

    for card in cards:

        try:
            nombre = card.find_element(By.XPATH,".//div[contains(@class, 'card-body')]//h3").text.strip()
        except:
            nombre = None

        try:
            precio = card.find_element(By.XPATH,".//div[contains(@class, 'price')]//a").text.strip()
            precio = int(precio.replace(",","").replace("$",""))
        except:
            precio = None
        
        try: 
            lugar_venta = card.find_element(By.XPATH,".//div[contains(@class, 'seller-location')]").text.strip()
        except:
            lugar_venta = None

        try:
            lis = card.find_elements(By.XPATH,".//div[contains(@class, 'key-details')]//li")
            caracteristicas = [li.text.strip() for li in lis]
            caracteristicas = " | ".join(caracteristicas)
        except:
            caracteristicas = None

        productos_csv.append([nombre, precio, lugar_venta, caracteristicas])

driver.quit()

with open(f'productos_{tienda}_{fecha}.csv', "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['Nombre', 'Precio', 'Lugar venta', 'Caracteristicas'])
    writer.writerows(productos_csv)
