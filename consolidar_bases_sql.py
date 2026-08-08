import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

#####  CON ESTO SOLO SE AGREGA EL ULTIMO SCRAP CON APPEND SE SUMA A LOS OTROS EN SQL  #####

load_dotenv()

csv_path = os.environ["CSV_PATH_SQL"]

fecha = datetime.now().strftime("%d-%m-%Y")
df_nuevo = pd.read_csv(csv_path, sep=",", encoding="utf-8")

#df = pd.concat([df_nuevo,df_antiguo], axis=0, ignore_index=True)

