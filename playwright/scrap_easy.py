from playwright.sync_api import sync_playwright
import csv
from datetime import datetime

playwright = sync_playwright().start()
browser = playwright.chromium.launch()
context = browser.new_context()
page = context.new_page()

products = []

tienda = "Easy"
fecha = datetime.now().strftime("%d-%m-%Y")

for pagina in range(1,7):

    url = f"https://www.easy.cl/search/maceteros?page={pagina}"

    page.goto(url)

    page.wait_for_selector("[data-testid= 'grid-container']")
    items = page.query_selector_all("[data-testid= 'grid-container']")

    for item in items:

        nombre = item.query_selector("[data-id^='product-name']")
        marca = item.query_selector("[data-id^='product-brand']")
        precio = item.query_selector("div.sc-94b513d4-42")

        if precio == None:
            precio = "sin precio"
        else:
            precio = precio.inner_text().replace(".","").replace("$","")

        #link = item.query_selector("xpath=..").get_attribute("href")

        nombre_val = nombre.inner_text()
        marca_val = marca.inner_text()
        

        products.append((nombre_val, marca_val, precio, tienda, fecha))


browser.close()
playwright.stop()

with open(f"productos_easy_{fecha}.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['Producto', 'Marca', 'Precio', 'Tienda', 'Fecha'])
    writer.writerows(products)