# Part 1*****************************************
#from bs4 import BeautifulSoup

#with open('Dummy.html', 'r') as html_file: 
#    content = html_file.read()
    #print(content)

#    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    #courses_tags = soup.find_all('h2')
    #print(courses_tags)
    
    #for courses in courses_tags:
    #   print(courses.text) 

#    course_cards = soup.find_all('div', class_="card")
#    for course in course_cards:
        #print(course.h5)
#        course_name = course.h5.text
#        course_price = course.a.text.split()[-1]

        #print(course_name)
        #print(course_price)
#        print(f'{course_name} costs {course_price}')

# Part 2*************************************
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://docs.openenergymonitor.org/').text
#print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
subchapter2 = soup.find_all('li', class_="toctree-l1")
#print(subchapter2)
for chapter in subchapter2:
    print(chapter.text)
    

#subchapter = soup.find('li', class_="toctree-l1")
#chaptertitle = subchapter.find('a', class_="reference internal").text
#print(chaptertitle)

#paragraphe = chaptertitle.find_all('p', class_='').text
#print(paragraphe)

#print(f'''
#Chapter : {subchapter2}
#Subchapter : {subchapter1}
#Title : 
#Paragraphes : {paragraphe}
#''')