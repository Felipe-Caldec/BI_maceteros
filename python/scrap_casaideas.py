from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from time import sleep
from time import time
import csv
import undetected_chromedriver as uc

"""opts = Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(
    service= Service(ChromeDriverManager().install()),
    options= opts
)"""
opts= uc.ChromeOptions()
driver= uc.Chrome(options=opts)

url = "https://www.casaideas.cl/search?q=maceteros"
driver.get(url)
sleep(6)

fecha = datetime.now().strftime("%d-%m-%Y")
tienda= "Casa ideas"

# scroll 
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
#######
productos_csv =[]

cards = driver.find_elements(By.XPATH, "//div[contains(@class,'ProductTile_product-details')]")

for card in cards:

    try:
        nombre = card.find_element(By.XPATH, ".//a[contains(@class, 'ProductTile_productname-link')]").text
    except:
        nombre = None


    try:
        precio = card.find_element(By.XPATH, ".//span[contains(text(), '$')]").text
        precio = int(precio)
    except:    
        precio = None

    productos_csv.append((nombre, precio, tienda, fecha))



driver.quit()


with open(f"productos_casaideas_{fecha}.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Producto", "Precio", "Tienda", "Fecha"])
    writer.writerows(productos_csv)










#https://www.amazon.com/-/es/s?k=maceteros&page=3&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=HSM2OTL9Y31&qid=1770328009&sprefix=maceter%2Caps%2C313&xpid=h_Kgv5puCYPgK&ref=sr_pg_3
#https://www.amazon.com/-/es/s?k=maceteros&page=2&xpid=h_Kgv5puCYPgK&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=HSM2OTL9Y31&qid=1770327991&sprefix=maceter%2Caps%2C313&ref=sr_pg_2
#https://www.amazon.com/-/es/s?k=maceteros&page=4&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=HSM2OTL9Y31&qid=1770328045&sprefix=maceter%2Caps%2C313&xpid=h_Kgv5puCYPgK&ref=sr_pg_4