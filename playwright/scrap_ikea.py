from playwright.sync_api import sync_playwright
import csv
from datetime import datetime


playwright= sync_playwright().start()
browser= playwright.chromium.launch()
context = browser.new_context()
page = context.new_page()

products = []

tienda = "Ikea"
fecha = datetime.now().strftime("%d-%m-%Y")

for pagina in range(1,6):

    url = f"https://www.ikea.com/cl/es/search/?q=macetero&page={pagina}"
    
    page.goto(url)

    page.wait_for_selector("[class = 'plp-mastercard__price-components']")
    items = page.query_selector_all("[class = 'plp-mastercard__price-components']")

    for item in items:

        nombre = item.query_selector("span.plp-price-module__description")
        marca = item.query_selector("span.plp-price-module__product-name")
        precio = item.query_selector("span.plp-price__integer")

        if precio == None:
            precio = "sin precio"
        else:
            precio = precio.inner_text().replace(".","")

        nombre_val = nombre.inner_text()
        marca_val = marca.inner_text()    

        products.append((nombre_val, marca_val, precio, tienda, fecha))

browser.close()
playwright.stop()

with open(f"productos_ikea_{fecha}.csv", "w", newline="", encoding="utf-8") as f:
    writer= csv.writer(f)
    writer.writerow(['Producto', 'Marca', 'Precio', 'Tienda', 'Fecha'])
    writer.writerows(products)