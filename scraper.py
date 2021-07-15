import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://oglobo.globo.com/")

doc = BeautifulSoup(response.text, 'html.parser')

titles = doc.select('h1[class*="title"] a') 

rows = []

for titulo in titles:
    row = {}
    row['title'] = titulo.text
    row['url'] = titulo.get('href')
    rows.append(row)

df = pd.DataFrame(rows)

df.to_csv("oglobo-headlines.csv")
