# Web scraper/crawler on botanical site 
# Translate into Excel -> different class (arbres, sapins, ..)
# Tranlate into Anki

from bs4 import BeautifulSoup

#with open("Dummy.html", "r") as f: #f = file
#    doc = BeautifulSoup(f, "html.parser")

#print(doc.prettify()) #to read the html file 

#<tag>

#tag = doc.title
#print(tag.string) #to access the content of the tag
#tag.string = "hello" # to change the content of a tag 
#tags = doc.find_all("p")[0]
#print(tags.find_all("b")) #display all elements with this tag 

import requests 

url = "https://www.conservation-nature.fr/plantes/adansonia/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
#print(doc.prettify())


especes = doc.find_all(text="espèces")
print(especes)
