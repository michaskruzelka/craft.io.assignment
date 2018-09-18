#!/usr/bin/python

import sys
import csv
from bs4 import BeautifulSoup


def main(arguments):
    """Extracts open jobs from specified html file and loads them to csv file"""
    with open(arguments[1], mode='w') as csv_file:
        fields = ['Job Title', 'Category', 'Status', 'Location']
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        with open(arguments[0], mode='r') as html_file:
            writerows(writer, html_file)


def writerows(writer, html_file):
    """Writes jobs rows into csv file"""
    print(type(writer), type(html_file))
    html = html_file.read()
    soup = BeautifulSoup(html, 'html.parser')
    sections_html = soup.find('section', attrs={"class": "roles-results"}).find_all('tbody')
    for section_html in sections_html:
        roles_html = section_html.find_all('tr')
        for role_html in roles_html:
            job_title = role_html.find('th').find('a').getText()
            category, status, location = ['; '.join([span.get_text() for span in td.find_all('span')])
                                          for td in role_html.find_all('td')]
            writer.writerow({'Job Title': job_title,
                             'Category': category,
                             'Status': status,
                             'Location': location})


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1:])
    else:
        print('No arguments specified')
