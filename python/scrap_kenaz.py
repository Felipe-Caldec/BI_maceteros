#https://www.kenaz.cl/search?options%5Bprefix%5D=last&options%5Bunavailable_products%5D=last&page=1&q=Macetero&type=product

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv
from datetime import datetime
from time import sleep

opts = Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(
    service= Service(ChromeDriverManager().install()),
    options= opts
)

tienda = "Kenaz"
fecha = datetime.now().strftime("%d-%m-%Y")

productos_csv = []

for pagina in range(1,5):
    url= f"https://www.kenaz.cl/search?options%5Bprefix%5D=last&options%5Bunavailable_products%5D=last&page={pagina}&q=Macetero&type=product"

    driver.get(url)
    sleep(6)

    cards = driver.find_elements(By.XPATH, "//div[contains(@class, 'sf__pcard-content')]")

    for card in cards:

        try:
            nombre = card.find_element(By.XPATH, ".//a[contains(@class, 'sf__pcard-name')]").text
        except:
            nombre = None

        try:
            precio = card.find_element(By.XPATH, ".//span[contains(@class, 'f-price-item--sale')]").text
            precio = precio.replace(".","").replace("$","").strip() # revisar nulos
        except:
            try:
                precio= card.find_element(By.XPATH, ".//div[contains(@class, 'f-price__regular')]//span[2]").text
                precio = precio.replace(".","").replace("$","").strip()
            except:    
                precio = None#//span[contains(@class, 'f-price-item--regular')]

        productos_csv.append((nombre, precio, tienda, fecha))

driver.quit()

with open(f"productos_kenaz_{fecha}_.csv", "w", newline="", encoding="utf-8") as f:
    
    writer= csv.writer(f)
    writer.writerow(["Producto", "Precio", "Tienda", "Fecha"])
    writer.writerows(productos_csv)

        