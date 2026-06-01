from playwright.sync_api import sync_playwright
import csv
from datetime import datetime

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()

products = []
tienda = "Casa Ideas"
fecha = datetime.now().strftime("%d-%m-%Y")
query = "maceteros"

url=f"https://www.casaideas.cl/search?q={query.replace(" ","-")}"

page.goto(url)

page.wait_for_selector("[class*='ProductTile_product-details']")

for _ in range(7):
    page.mouse.wheel(0, 1200)
    page.wait_for_timeout(2000)

items = page.query_selector_all("[class*= 'ProductTile_product-details']")

for item in items:

    nombre = item.query_selector("[class*='ProductTile_productname-link']")

    precio = (
        item.query_selector("[class*='ProductPrice_total-price']")
        or item.query_selector("[class*='ProductPrice_subtotal-price']")
    ) # NO FUNCIONA TRY/EXCEPT PORQUE NO LANZA ERROR POR LO TANTO NUNCA TOMA EXCEPT

    nombre_val = nombre.inner_text()
    precio_val = precio.inner_text().replace(".","").replace("$","")

    products.append((nombre_val, precio_val, tienda, fecha))

browser.close()
playwright.stop()

with open(f"productos_casaideas_{fecha}.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['Producto', 'Precio', 'Tienda', 'Fecha'])
    writer.writerows(products)
