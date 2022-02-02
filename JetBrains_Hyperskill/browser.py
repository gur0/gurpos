import os
import sys
import shutil
import requests
from bs4 import BeautifulSoup

'''
nytimes_com = "https://www.nytimes.com/"
bloomberg_com = "https://www.bloomberg.com/"
USER_AGENT = 'Mozilla/5.0'

def visit_url(url):
    if not url.startswith("http"):
        url = "https://" + url
    r = requests.get(url, headers={'User-Agent': USER_AGENT})
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
    elif r.status_code == 404:
        sys.exit()
    return soup
'''
dir_name = sys.argv[1]

def print_url(src_name):
    page = f'''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
of Apollo 11, and Neil Armstrong -- the first man to walk
on the moon. It was the height of the Cold War, and the charts
were filled with David Bowie's Space Oddity, and Creedence's
Bad Moon Rising. The world is a very different place than
it was 5 decades ago. But how has the space race changed since
the summer of '69? (Source: {src_name})


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey
addressed Apple Inc. employees at the iPhone maker’s headquarters
Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''
    print(page)
    return page

def print_bloom(src_name="Bloomberg"):
    return print_url(src_name)

def print_nytime(src_name="New York Times"):
    return print_url(src_name)

bloomberg_com = ''
nytimes_com = ''
def print_auto(url):
    global bloomberg_com
    global nytimes_com
    if url.find('bloomberg') >= 0:
        bloomberg_com = print_bloom()
        urls['bloomberg.com'] = bloomberg_com
        return 'bloomberg'
    elif url.find('nytimes') >= 0:
        nytimes_com = print_nytime()
        urls['nytimes.com'] = nytimes_com
        return 'nytimes'
    return ''

urls = {'bloomberg.com': bloomberg_com, 'nytimes.com': nytimes_com}

def check_url(url):
    if url.find('.') > 0:
        if url in urls.keys():
            return True
    return False

def file_write(file_path, file_content):
    file = open(file_path, 'w')
    file.write(file_content)
    file.close()

if not os.access(dir_name, os.F_OK):
    os.mkdir(dir_name)

while True:
    url = input()
    if url == 'exit':
        break
    if os.access(dir_name + os.path.sep + url, os.R_OK):
        print_auto(url)
    else:
        if check_url(url):
            ret = print_auto(url)
            fname = dir_name + os.path.sep + ret
            file_write(fname, urls[url])
        else:
            print('Error: Incorrect URL')
'''
    sp = visit_url(url)
'''
