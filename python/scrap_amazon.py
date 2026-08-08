from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from time import sleep
import csv
import time
import undetected_chromedriver as uc

"""opts = Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(
    service= Service(ChromeDriverManager().install()),
    options= opts 
)
"""
opts= uc.ChromeOptions()
driver= uc.Chrome(options=opts)

tienda = "Amazon"
fecha = datetime.now().strftime('%d-%m-%Y')
productos_csv = []

url = "https://www.amazon.com/s?k=maceteros&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2WKDO0QNPFM14&sprefix=maceteros%2Caps%2C301&ref=nb_sb_noss_1"
driver.get(url)
sleep(6)


duracion = 60  # segundos

end_time = time.time() + duracion

while time.time() < end_time:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

cards = driver.find_elements(By.XPATH, '//div[contains(@class, "puis-card-container")]')

for card in cards:

    try:
        nombre = card.find_element(By.XPATH, './/div[contains(@data-cy, "title-recipe")]//h2/span').text.strip()
    except:
        nombre = None

    try:
        precio = card.find_element(By.XPATH, './/span[contains(@class, "a-price-whole")]').text.strip()
        precio = int(precio.replace('CLP',"").replace(',',''))
    except:
        precio = None
        
    try:
        precio_envio = card.find_element(By.XPATH, './/div[contains(@data-cy, "delivery-block")]/div[2]/div').text.strip()
    except:
        precio_envio = None

    productos_csv.append([nombre, precio, precio_envio, tienda, fecha])

driver.quit()

with open(f'productos_amazon_{fecha}.csv', "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['Producto', 'Precio','Precio envio', 'Tienda', 'Fecha'])
    writer.writerows(productos_csv)