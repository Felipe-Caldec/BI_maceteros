from playwright.sync_api import sync_playwright
import csv
from datetime import datetime

playwright = sync_playwright().start()
browser = playwright.chromium.launch()
context = browser.new_context()
page = context.new_page()

products=[]

tienda = "Amazon"
fecha = datetime.now().strftime("%d-%m-%Y")

for pagina in range(1,8):
    base_url = "https://www.amazon.com/s?k=maceteros&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2WKDO0QNPFM14&sprefix=maceteros%2Caps%2C301&ref=nb_sb_noss_1"
    if pagina == 1:
         url = base_url
    else:
         url = f"https://www.amazon.com/-/es/s?k=maceteros&page={pagina}&xpid=qUBBKdPs3gv4D&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2WKDO0QNPFM14&qid=1772143144&sprefix=maceteros%2Caps%2C301&ref=sr_pg_2"

    page.goto(url)
    
    page.wait_for_selector("div.puis-card-container")
    items = page.query_selector_all("div.puis-card-container")

    
    for item in items:

            nombre= item.query_selector("[data-cy = title-recipe]") 
            precio= item.query_selector("span.a-price-whole")
            precio_envio = item.query_selector("[data-cy=delivery-block]")

            if precio == None:
                precio = "sin precio"
            else:
                precio = precio.inner_text().replace(",","")
            
            if precio_envio == None:
                precio_envio = "sin precio"
            else:
                precio_envio = precio_envio.inner_text().replace(",","")

            nombre_val = nombre.inner_text()


            products.append((nombre_val, precio, precio_envio, tienda, fecha))

browser.close()
playwright.stop() 

with open(f"productos_amazon_{fecha}.csv", "w", newline="", encoding="utf-8") as f:
    writer= csv.writer(f)
    writer.writerow(['Producto', 'Precio', 'Precio envio', 'Tienda', 'Fecha'])
    writer.writerows(products)