import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
<<<<<<< HEAD
import os
from dotenv import load_dotenv

#####  CON ESTO SOLO SE AGREGA EL ULTIMO SCRAP CON APPEND SE SUMA A LOS OTROS EN SQL  #####

load_dotenv()

csv_path = os.environ["CSV_PATH_SQL"]

fecha = datetime.now().strftime("%d-%m-%Y")
df_nuevo = pd.read_csv(csv_path, sep=",", encoding="utf-8")

#df = pd.concat([df_nuevo,df_antiguo], axis=0, ignore_index=True)

=======

#####  CON ESTO SOLO SE AGREGA EL ULTIMO SCRAP CON APPEND SE SUMA A LOS OTROS EN SQL  #####

fecha = datetime.now().strftime("%d-%m-%Y")
df_nuevo = pd.read_csv(r"C:\Users\olgac\OneDrive\Desktop\scrapping\consolidado_precio_productos_04-03-2026.csv", sep=",", encoding="utf-8")
#df_antiguo = pd.read_csv(r"C:\Users\olgac\OneDrive\Desktop\scrapping\consolidado_precio_productos_03-03-2026.csv", sep=",", encoding="utf-8")

#df = pd.concat([df_nuevo,df_antiguo], axis=0, ignore_index=True)

engine = create_engine(
    "postgresql+psycopg2://postgres:1234@localhost:5432/scrap_maceteros"
)

df_nuevo.to_sql(name="productos",con=engine, if_exists="append",  # "fail" | "replace" | "append"
    index=False
)
>>>>>>> 69ec57f8e3ed5eed9dde2bf24b94a8c116ef9932
