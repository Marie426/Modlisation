from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://docs.openenergymonitor.org/electricity-monitoring/index.html').text
soup = BeautifulSoup(html_text, 'lxml')

Learn_page = soup.find('div', class_="toctree-wrapper compound")
# For Electricity Monitoring
print(Learn_page.text)
section1 = Learn_page.find('li', class_="toctree-l1")
#print(section1)

title_page1 = section1.find('li', class_="toctree-l2").text
#print(title_page1)
page1 = section1.find('li', class_="toctree-l2")
insidetext1 = page1.find('a', href_=True)
#print(page1)

soup2 = BeautifulSoup(html_text, "html.parser")

for link in soup.find_all("a"):
    sub_url = link.get("href")
    sub_response = requests.get(sub_url)
    sub_soup = BeautifulSoup(sub_response.text, "html.parser")

section = soup.find_all('li', class_="toctree-l1")
#for page in pages:
    #print(page.text)