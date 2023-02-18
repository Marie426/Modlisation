import requests
from bs4 import BeautifulSoup

url = "https://docs.openenergymonitor.org/learn/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the main content container
main_content = soup.find_all("div", class_="main-content-inner")

# Extract the text from the main content container
if main_content:
    text = main_content[0].get_text("\n")
else:
    text=""

# Write the text to a file
with open("learn_text.txt", "w") as f:
    f.write(text)

print("Text saved to file 'learn_text.txt'.")
#___________________________________________________
