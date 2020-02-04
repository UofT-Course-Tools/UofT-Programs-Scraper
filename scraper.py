from bs4 import BeautifulSoup
import requests
import json
from category import Category
from program import Program

# testing to see if I can get every program link
"""
source = requests.get(
    "https://student.utm.utoronto.ca/calendar//program_list.pl").text
soup = BeautifulSoup(source, 'lxml')

program_links = []
program_link = "https://student.utm.utoronto.ca/calendar//"
content = soup.find_all('div', class_="normaltext")[1]
for section in content.find_all('ul'):
    for program in section.find_all('li'):
        print(program.text)
        program_link += program.a['href']
        program_links.append(program_link)
        program_link = "https://student.utm.utoronto.ca/calendar//"

[print(x + "\n") for x in program_links]
"""
source = requests.get("https://student.utm.utoronto.ca/calendar//program_group.pl?Group_Id=9").text
soup = BeautifulSoup(source, 'lxml')

# scrapping 
# print(soup.prettify())
category = Category()
title_field = soup.find('p',class_='titlestyle').text.split(' ')
name = ' '.join(title_field[:-1])   
degrees = title_field[-1].strip('(').strip(')').split(',')
all_info = soup.find('div', class_='contentpos')
description = all_info.contents[10]
print(description)


# adding to object
category.set_name(name)
category.set_program_type(3)
category.set_description(description)

for degree in degrees:
    category.add_degrees(degree)




print(category.name)
print(category.degrees)
# print(category.description)









