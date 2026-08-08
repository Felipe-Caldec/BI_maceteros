# https://www.construmart.cl/jardin/maceteros-y-deco?cat=1139%2C680

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pickle
from time import sleep

# guardar cookies
opts = Options()
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

driver.get("https://www.construmart.cl/?srsltid=AfmBOopKAII3FxZkGFl-_wyKVdU0fXUz11Cqm8sLceM_xpe2V_RsYnep")

print("Selecciona región y comuna manualmente...")
sleep(30)   # tienes 30 segundos para hacerlo a mano


pickle.dump(driver.get_cookies(), open("cookies_construmart_departa", "wb"))


print("Cookies guardadas.")

cookies = driver.get_cookies()
driver.quit()
print("Total cookies:", len(cookies))
pickle.dump(cookies, open("cookies_construmart_departa.pkl", "wb"))