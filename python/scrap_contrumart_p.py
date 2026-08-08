import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
import csv
import undetected_chromedriver as uc

opts = Options()
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

"""opts = uc.ChromeOptions()
driver = uc.Chrome(options=opts)"""
driver.get("https://www.construmart.cl/")

# cargar cookies
for cookie in pickle.load(open("cookies_construmart_departa.pkl", "rb")):
    driver.add_cookie(cookie)

# refrescar con sesión ya seteada
driver.refresh()

tienda = "Construmart"
fecha = datetime.now().strftime("%d-%m-%Y")
productos_csv= []
base_url = "https://www.construmart.cl/jardin/maceteros-y-deco?cat=1139%2C680"


for pagina in range(1, 6):  # 10 páginas = ~500 productos
    if pagina == 1:
        url = base_url
    else:
        url = f'{base_url}&p={pagina}'

    print("Scrapeando:", url)

    driver.get(url)
    sleep(5)

    cards = driver.find_elements(By.XPATH, "//div[contains(@class,'product-item-details')]")

    for card in cards:
        try:
            nombre = card.find_element(
                By.XPATH, ".//a[contains(@class,'product-item-link')]"
            ).text.strip()
        except:
            nombre = None

        try:
            marca = card.find_element(
                By.XPATH, ".//p[contains(@class,'atributte-brand')]"
            ).text.strip()
        except:
            marca = None

        try:
            precio = card.find_element(
                By.XPATH,
                ".//div[contains(@class,'price-box')]//span[contains(@class,'price')]"
            ).text.strip()
            precio = int(precio.replace("$","").replace(".", "").strip())
        except:
            precio = None
            
        productos_csv.append((nombre, marca, precio, tienda, fecha))

driver.quit()

productos_csv_nuevo =[]
for y in productos_csv:
    if y[0] is not None:
        productos_csv_nuevo.append(y)


with open(f"productos_construmart_{fecha}.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Producto","Marca", "Precio", "Tienda", "Fecha"])
    writer.writerows(productos_csv_nuevo)

print("Total productos:", len(productos_csv))