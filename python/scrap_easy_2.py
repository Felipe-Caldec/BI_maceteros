from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import csv

# sc-2b846afc-67 esas clases no son confiables porque se hacen con React es decir son dinamicas
# no extrae info

opts = Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

productos_csv = []

for pagina in range(1, 6):  # 10 páginas = ~500 productos
    url = f"https://www.easy.cl/search/maceteros?page={pagina}"
    print("Scrapeando:", url)

    driver.get(url)
    sleep(6)

    cards = driver.find_elements(By.XPATH, "//div[@data-id='product-card']")

    for card in cards:
        try:
            nombre = card.find_element(By.XPATH, ".//span[contains(@data-id,'product-name')]").text
        except:
            nombre = None

        try:
            marca = card.find_element(By.XPATH,".//span[contains(@data-id,'product-brand')]").text
        except:
            marca = None

        try:
            precio = card.find_element(By.XPATH,".//div[contains(text(),'$')]").text
            precio = int(precio.replace("$","").replace(".","").strip())
        except:
            precio = None

        productos_csv.append((nombre, marca, precio))

driver.quit()

with open("productos_easy.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Producto","Marca", "Precio"])
    writer.writerows(productos_csv)


