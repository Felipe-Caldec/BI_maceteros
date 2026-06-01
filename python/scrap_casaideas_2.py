from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from time import sleep
from time import time
import csv


opts = Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(
    service= Service(ChromeDriverManager().install()),
    options= opts
)
url = "https://www.casaideas.cl/search?q=maceteros"
driver.get(url)
sleep(6)

fecha = datetime.now().strftime("%d-%m-%Y")
tienda= "Casa ideas"

# scroll 
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
#######
productos_csv =[]

cards = driver.find_elements(By.XPATH, "//div[contains(@class,'ProductTile_product-details')]")

for card in cards:
    try:
        nombre = card.find_element(By.XPATH, ".//a[contains(@class, 'ProductTile_productname-link')]").text
    except:
        nombre = None
    try:
        precio = card.find_element(By.XPATH, ".//span[contains(@class, 'ProductPrice_total-price')]").text
        precio = int(precio.replace("$","").replace(".",""))
    except:    
        try:
            precio = card.find_element(By.XPATH, ".//span[contains(@class,'ProductPrice_subtotal-price')]").text
            precio = int(precio.replace("$","").replace(".","")) ## revisar
        except:
            precio = None

    productos_csv.append((nombre, precio, tienda, fecha))



driver.quit()


with open(f"productos_casaideas_{fecha}.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Producto", "Precio", "Tienda", "Fecha"])
    writer.writerows(productos_csv)








