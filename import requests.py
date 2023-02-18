import requests
from bs4 import BeautifulSoup

url = "https://www.conservation-nature.fr/plantes/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

species_list = []
for species_item in soup.find_all("div", class_="biblio_liste_plante"):
    species_name = species_item.find("a").text
    species_list.append(species_name)

print(species_list)