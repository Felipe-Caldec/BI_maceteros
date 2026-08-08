from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from time import sleep
import csv
import undetected_chromedriver as uc

opts = Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(
    service= Service(ChromeDriverManager().install()),
    options = opts
)

"""opts = uc.ChromeOptions()
driver = uc.Chrome(options=opts)"""

fecha = datetime.now().strftime('%d-%m-%Y')
tienda = "Paris"
productos_csv = []


for pagina in range(1,8):
    url = f"https://www.paris.cl/search/?q=maceteros&page={pagina}"

    driver.get(url)
    sleep(6)

    cards = driver.find_elements(By.XPATH, "//div[contains(@data-testid, 'paris-vertical-pod')]")

    for card in cards:

        try:
            nombre = card.find_element(By.XPATH, ".//div/div[3]/div[2]/span[2]").text.strip()
        except:
            nombre = None

        try:
            marca = card.find_element(By.XPATH, ".//div/div[3]/div[2]/span[1]").text.strip()
        except:
            marca = None

        try:
            precio = card.find_element(By.XPATH,".//div[contains(@data-testid, 'paris-pod-price')]//span" ).text.strip()
            precio = int(precio.replace('$',"").replace('.',''))
        except:
            precio = None

        productos_csv.append([nombre, marca, precio, tienda, fecha])

driver.quit()

with open(f"productos_paris_{fecha}.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['Producto', 'Marca', 'Precio', 'Tienda', 'Fecha'])
    writer.writerows(productos_csv)

    