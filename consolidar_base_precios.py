import pandas as pd
from datetime import datetime

df_sodimac = pd.read_csv(r"C:\Users\olgac\OneDrive\Desktop\scrapping\lista_productos_sodimac_04-03-2026_test.csv", sep=",",encoding="utf-8")
df_easy = pd.read_csv(r"C:\Users\olgac\OneDrive\Desktop\scrapping\lista_productos_easy_04-03-2026_test.csv", sep=",", encoding="utf-8")
df_mercado_libre = pd.read_csv(r"C:\Users\olgac\OneDrive\Desktop\scrapping\lista_productos_ml_04-03-2026_test.csv", sep=",", encoding="utf-8")
df_construmart = pd.read_csv(r"C:\Users\olgac\OneDrive\Desktop\scrapping\lista_productos_construmart_04-03-2026_test.csv", sep=",", encoding="utf-8")
df_casaideas = pd.read_csv(r"C:\Users\olgac\OneDrive\Desktop\scrapping\lista_productos_casaideas_04-03-2026_test.csv", sep=",", encoding="utf-8")
df_ikea = pd.read_csv(r"C:\Users\olgac\OneDrive\Desktop\scrapping\lista_productos_ikea_04-03-2026_test.csv", sep=",", encoding="utf-8")
#df_kenaz = pd.read_csv(r"C:\Users\olgac\OneDrive\Desktop\scrapping\csv\lista_productos_kenaz_06-02-2026_clean.csv", sep=",", encoding="utf-8")
df_plantme = pd.read_csv(r"C:\Users\olgac\OneDrive\Desktop\scrapping\lista_productos_plantme_04-03-2026_test.csv", sep=",", encoding="utf-8")
df_amazon = pd.read_csv(r"C:\Users\olgac\OneDrive\Desktop\scrapping\lista_productos_amazon_04-03-2026_test.csv", sep=",", encoding="utf-8")
df_paris = pd.read_csv(r"C:\Users\olgac\OneDrive\Desktop\scrapping\lista_productos_paris_04-03-2026_test.csv", sep=",", encoding="utf-8")

#consolidado = pd.read_excel()

fecha = datetime.now().strftime("%d-%m-%Y")

consolidado = pd.concat([ df_easy, df_mercado_libre, df_sodimac, df_construmart,
                         df_plantme, df_ikea, df_casaideas, df_paris,df_amazon ], axis=0)

consolidado['Precio'] = consolidado["Precio"].astype("Int64")
consolidado['Fecha'] = consolidado["Fecha"].astype("string")

#print(type(consolidado['Precio']))
consolidado.to_csv(f"consolidado_precio_productos_{fecha}.csv")