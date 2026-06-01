
from playwright.sync_api import sync_playwright
import polars as pl
import csv
from datetime import datetime

playwright = sync_playwright().start()
browser = playwright.chromium.launch()
context = browser.new_context()
page = context.new_page()

products = []

tienda = "Sodimac"
fecha = datetime.now().strftime("%d-%m-%Y")

for pagina in range(1,7):

    url = f"https://www.sodimac.cl/sodimac-cl/lista/CATG10520/Maceteros-y-Accesorios?page={pagina}&store=so_com"
    page.goto(url)

    page.wait_for_selector("div.grid-pod")
    items = page.query_selector_all("div.grid-pod")

    for item in items:
        nombre = item.query_selector("b.pod-subTitle")
        marca = item.query_selector("b.pod-title")
        precio = item.query_selector("div.cross-price-item")
        
        if precio == None:
            precio = "sin precio"
        else:
            precio = precio.inner_text().replace(".","").replace("$","")
        
        #link = item.get_attribute("a")

        nombre_val = nombre.inner_text()
        marca_val = marca.inner_text()
        

        products.append((nombre_val,marca_val, precio, tienda, fecha))

print(len(products))

browser.close()
playwright.stop()

with open(f"productos_sodimac_{fecha}.csv", "w", newline="", encoding="utf-8") as f:
    writer= csv.writer(f)
    writer.writerow(['Producto', 'Marca', 'Precio', 'Tienda', 'Fecha'])
    writer.writerows(products)





