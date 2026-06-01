from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import csv


# Busqueda por "Maceteros" en ML
opts = Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/135.0.7049.115 Safari/537.36")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

driver.get("https://listado.mercadolibre.cl/maceteros?sb=all_mercadolibre#D[A:maceteros]")
sleep(8)

# ---------- SCROLL LAZY LOADING ----------
last_count = 0
retries = 0

while True:
    productos = driver.find_elements(By.XPATH, "//div[contains(@class,'poly-card')]")

    if len(productos) == last_count:
        retries += 1
        if retries > 3:
            break
    else:
        last_count = len(productos)
        retries = 0

    driver.execute_script("arguments[0].scrollIntoView();", productos[-1])
    sleep(3)

# ---------- EXTRACCIÓN CORRECTA ----------
cards = driver.find_elements(By.XPATH, "//div[contains(@class,'poly-card')]")

productos_csv = []

for card in cards:
    try:
        nombre = card.find_element(
            By.XPATH,
            ".//a[contains(@class,'poly-component__title')]"
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

    productos_csv.append((nombre, precio))

# ---------- GUARDAR CSV ----------
with open("productos_mercado_libre.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Producto", "Precio"])
    writer.writerows(productos_csv)

driver.quit()
print("✅ CSV generado correctamente")
