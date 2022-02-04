import os
import sys
import shutil
import requests
from bs4 import BeautifulSoup

USER_AGENT = 'Mozilla/5.0'

def visit_url(url):
    if not url.startswith("http"):
        url = "https://" + url
    r = requests.get(url, headers={'User-Agent': USER_AGENT})
    if r.status_code == 200:
        sp = BeautifulSoup(r.content, 'html.parser')
        for data in sp(['style', 'script']):
            # Remove tags
            data.decompose()
        # soup = r.text
        soup = ' '.join(sp.stripped_strings)
    elif r.status_code == 404:
        sys.exit()
    return soup

dir_name = sys.argv[1]

def print_url(src_url):
    page = visit_url(src_url)
    print(page)
    return page

other_com = ''

def print_auto(url):
    global other_com
    other_com = print_url(url)
    urls[url] = other_com
    return url.split('.')[0]

urls = {}

def check_url(url):
    if url.find('.') > 0:
        return True
    return False

def file_write(file_path, file_content):
    file = open(file_path, 'w')
    file.write(file_content)
    file.close()

if not os.access(dir_name, os.F_OK):
    os.mkdir(dir_name)

history = []

while True:
    url = input()
    if url == 'exit':
        break
    elif url == 'back':
        if len(history) == 0:
            continue
        history.pop()
        url = history.pop()
        history.append(url)
    if os.access(dir_name + os.path.sep + url, os.R_OK):
        print_auto(url)
        history.append(url)
    else:
        if check_url(url):
            ret = print_auto(url)
            history.append(url)
            fname = dir_name + os.path.sep + ret
            file_write(fname, urls[url])
        else:
            print('Error: Incorrect URL')
