#https://plantme.cl/collections/maceteros-oficial?page=1

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import csv
from time import sleep
import undetected_chromedriver as uc

opts = Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(
    service= Service(ChromeDriverManager().install()),
    options= opts
)

"""opts = uc.ChromeOptions()

driver= uc.Chrome(options=opts)"""

tienda = "Plantme"
fecha = datetime.now().strftime("%d-%m-%Y")

productos_csv =[]

for pagina in range(1,6):
    url = f"https://plantme.cl/collections/maceteros-oficial?page={pagina}"

    driver.get(url)
    sleep(6)

    cards = driver.find_elements(By.XPATH, "//div[contains(@class, 'grid-item__content')]")

    for card in cards:

        try:
            nombre = card.find_element(By.XPATH, ".//div[contains(@class, 'grid-product__title')]").text
        except:
            nombre = None

        try:
            precio = card.find_element(By.XPATH, ".//span[contains(@class, 'grid-product__price--current')]//span[@aria-hidden='true']").text
            precio = int(precio.replace(".","").replace("$",""))
        except:
            precio = None

        productos_csv.append((nombre, precio, tienda, fecha))


driver.quit()

with open(f"productos_plantme_{fecha}.csv", "w", newline="", encoding="utf-8") as f:
    
    write = csv.writer(f)
    write.writerow(["Producto", "Precio", "Tienda", "Fecha"])
    write.writerows(productos_csv)


