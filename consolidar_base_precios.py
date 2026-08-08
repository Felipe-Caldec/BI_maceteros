import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

path_sodimac = os.environ['PATH_SODIMAC']
path_easy  = os.environ['PATH_EASY']
path_mercado_libre  = os.environ['PATH_MERCADO_LIBRE']
path_construmart = os.environ['PATH_CONSTRUMART']
path_casaideas = os.environ['PATH_CASAIDEAS']
path_ikea = os.environ['PATH_IKEA']
path_plantme = os.environ['PATH_PLANTME']
path_amazon = os.environ['PATH_AMAZON']
path_paris = os.environ['PATH_PARIS']


df_sodimac = pd.read_csv(path_sodimac, sep=",",encoding="utf-8")
df_easy = pd.read_csv(path_easy, sep=",", encoding="utf-8")
df_mercado_libre = pd.read_csv(path_mercado_libre, sep=",", encoding="utf-8")
df_construmart = pd.read_csv(path_construmart, sep=",", encoding="utf-8")
df_casaideas = pd.read_csv(path_casaideas, sep=",", encoding="utf-8")
df_ikea = pd.read_csv(path_ikea, sep=",", encoding="utf-8")
df_plantme = pd.read_csv(path_plantme, sep=",", encoding="utf-8")
df_amazon = pd.read_csv(path_amazon, sep=",", encoding="utf-8")
df_paris = pd.read_csv(path_paris, sep=",", encoding="utf-8")

#consolidado = pd.read_excel()

fecha = datetime.now().strftime("%d-%m-%Y")

consolidado = pd.concat([ df_easy, df_mercado_libre, df_sodimac, df_construmart,
                         df_plantme, df_ikea, df_casaideas, df_paris,df_amazon ], axis=0)

consolidado['Precio'] = consolidado["Precio"].astype("Int64")
consolidado['Fecha'] = consolidado["Fecha"].astype("string")

#print(type(consolidado['Precio']))
consolidado.to_csv(f"consolidado_precio_productos_{fecha}.csv")