import requests
from bs4 import BeautifulSoup
import python-docx

# Step 1: Retrieve the HTML content of the page
url = "https://docs.openenergymonitor.org/"
response = requests.get(url)
html_content = response.content

# Step 2: Extract the relevant text and hyperlinks
soup = BeautifulSoup(html_content, "html.parser")
learn_section = soup.find("section", {"id": "learn"})
text = ""
for p in learn_section.find_all("p"):
    text += p.text

# Step 3: Extract text from linked pages
links = []
for a in learn_section.find_all("a"):
    links.append(a["href"])

for link in links:
    response = requests.get(link)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    text += soup.get_text()

# Step 4: Compile all the extracted text into a single string
full_text = text

# Step 5: Create a new Word document and insert the text
doc = python-docx.Document()
doc.add_paragraph(full_text)
doc.save("learn_section.docx")

#*********************************************************
import requests
from bs4 import BeautifulSoup
import python-docx

# Step 1: Retrieve the HTML content of the page
url = "https://docs.openenergymonitor.org/"
try:
    response = requests.get(url)
    response.raise_for_status()
    html_content = response.content
except requests.exceptions.RequestException as e:
    print(f"Request to {url} failed: {e}")
    exit(1)

# Step 2: Extract the relevant text and hyperlinks
soup = BeautifulSoup(html_content, "html.parser")
learn_section = soup.find("section", {"id": "learn"})
text = ""
for p in learn_section.find_all("p"):
    text += p.text

# Step 3: Extract text from linked pages
links = []
for a in learn_section.find_all("a"):
    links.append(a["href"])

for link in links:
    try:
        response = requests.get(link)
        response.raise_for_status()
        html_content = response.content
    except requests.exceptions.RequestException as e:
        print(f"Request to {link} failed: {e}")
        continue
    soup = BeautifulSoup(html_content, "html.parser")
    text += soup.get_text()

# Step 4: Compile all the extracted text into a single string
full_text = text

# Step 5: Create a new Word document and insert the text
try:
    doc = python-docx.Document()
    doc.add_paragraph(full_text)
    doc.save("learn_section.docx")
except Exception as e:
    print(f"Failed to create Word document: {e}")
    exit(1)