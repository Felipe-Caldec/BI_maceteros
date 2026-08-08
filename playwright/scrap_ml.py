
from playwright.sync_api import sync_playwright
import csv
from datetime import datetime


playwright = sync_playwright().start()
browser = playwright.firefox.launch()
context = browser.new_context()
page = context.new_page()

query = "maceteros"
base_url = f"https://listado.mercadolibre.cl/{query.replace(" ","-")}"
products = []

tienda = "Mercado Libre"
fecha = datetime.now().strftime("%d-%m-%Y")

for offset in range(1,289,48):

    url=f"{base_url}/hogar-muebles/jardin-aire-libre/decoracion-exterior/macetas-maceteros/nuevo/macetero_Desde_{offset}_NoIndex_True?sb=all_mercadolibre"
    
    page.goto(url)

    page.wait_for_selector("li.ui-search-layout__item")
    items = page.query_selector_all("li.ui-search-layout__item")

    for item in items:
        title = item.query_selector("h3")
        price = item.query_selector("span.andes-money-amount__fraction")
        nota = item.query_selector("span.poly-phrase-label")

        if nota == None:
            nota = "sin nota"
        else:
            nota = nota.inner_text()

        #link = item.query_selector("a").get_attribute("href")

        title_val = title.inner_text()
        price_val = price.inner_text().replace(".","")
        products.append((title_val,price_val, nota, tienda, fecha))

print(len(products))

browser.close()
playwright.stop()

with open(f"productos_ml_{fecha}.csv", "w", newline="", encoding="utf-8") as f:
    writer= csv.writer(f)
    writer.writerow(['Producto', 'Precio', 'Nota', 'Tienda', 'Fecha'])
    writer.writerows(products)