#!/usr/bin/python

import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


def main(arguments):
    """Extracts html code from specified url"""
    # html = urlopen(arguments[0])
    # with open(arguments[1], 'w', encoding='utf-8') as file:
    #     file.write(html.read().decode('utf8'))
    browser = webdriver.Chrome()
    browser.get(arguments[0])
    try:
        WebDriverWait(browser, 10).until(lambda x: x.find_element_by_class_name('roles-results'))
    except TimeoutException:
        print('Couldn\'t find roles container')
        exit(1)
    with open(arguments[1], 'w', encoding='utf-8') as file:
        file.write(browser.page_source)
        browser.close()


if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1:])
    else:
        print('No arguments specified')
