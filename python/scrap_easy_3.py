from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import datetime
import csv
import undetected_chromedriver as uc

# sc-2b846afc-67 esas clases no son confiables porque se hacen con React es decir son dinamicas
# no extrae info
# termino funcionando con estas clases (sc-2b846afc-67) quizas haya que actualizar con el tiempo
# trae 200 productos con marca y precio


# cards = driver.find_elements(By.XPATH, "//div[@data-testid='grid-container']") funciono para traer precio

opts = Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

"""opts = uc.ChromeOptions()
driver = uc.Chrome(options=opts)"""

fecha = datetime.now().strftime("%d-%m-%Y")
tienda= "Easy"

productos_csv = []

for pagina in range(1, 2):  # 10 páginas = ~500 productos
    url = f"https://www.easy.cl/search/maceteros?page={pagina}"
    print("Scrapeando:", url)

    driver.get(url)
    sleep(6)

    cards = driver.find_elements(By.XPATH, "//div[@data-testid='grid-container']")

    for card in cards:
        try:
            nombre = card.find_element(By.XPATH, ".//div[contains(@class,'sc-94b513d4-4')]//span[contains(@class,'sc-94b513d4-6')]").text
        except:
            nombre = None

        try:
            marca = card.find_element(By.XPATH,".//div[contains(@class,'sc-94b513d4-4')]//span[contains(@class,'sc-94b513d4-5')]" ).text
        except:
            marca = None 

        try:
            precio = card.find_element(By.XPATH,".//div[contains(text(),'$')]").text
            precio = int(precio.replace("$","").replace(".","").strip())
        except:
            precio = None

        """try:
            link = card.find_element(By.XPATH,"..").get_attribute("href")
        except:
            link = None """ # el ".." hace ref a contenedor padre  "../h2" --> etiqueta dentro del padre

        productos_csv.append((nombre, marca, precio, tienda, fecha))

driver.quit()

with open(f"productos_easy_{fecha}.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Producto","Marca", "Precio", "Tienda", "Fecha"])
    writer.writerows(productos_csv)