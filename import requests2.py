import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.conservation-nature.fr/types/arbre/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

species_data = []
for species_item in soup.find_all("p", class_="nom_latin"):
    species_name = species_item.find("a").text
    species_data.append({"Species Name": species_name})


species_df = pd.DataFrame(species_data)
species_df.to_csv("species_info.csv", index=False)
