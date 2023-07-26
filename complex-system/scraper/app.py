import datetime
import time
import pandas as pd
import os

url = "https://fr.wikipedia.org/wiki/Top_250_de_l%27Internet_Movie_Database"

df = pd.read_html(url)[0]


while True:
    now = datetime.datetime.now().isoformat().replace(".", "_")
    filename = f"top_250_imdb_{now}.csv"

    os.makedirs('data', exist_ok=True)
    df.to_csv(f'/usr/src/app/data/{filename}')

    time.sleep(60)