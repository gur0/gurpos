import os
import sys
import requests

from bs4 import BeautifulSoup

t_lang = ['Arabic', 'German', 'English', 'Spanish', 'French',
          'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese',
          'Romanian', 'Russian', 'Turkish']

def lang_string_index(langs):
    global t_lang
    if langs == 'all':
        return 0
    idx = 0
    for l in t_lang:
        idx += 1
        if l.lower() == langs:
            return idx
    return -1

origin_lang = lang_string_index(sys.argv[1])
target_lang = lang_string_index(sys.argv[2])
word = sys.argv[3]

if origin_lang == -1:
    print("Sorry, the program doesn't support", sys.argv[1])
    sys.exit()
if target_lang == -1:
    print("Sorry, the program doesn't support", sys.argv[2])
    sys.exit()

f = open(f'{word}.txt', "w+")

USER_AGENT = 'Mozilla/5.0'

def my_print(line):
    global f
    f.write(line + '\n')
    print(line)

def my_translator(org_lang, trg_lang):
    global word
    global t_lang
    lang_lang = f'{t_lang[org_lang-1]}-{t_lang[trg_lang-1]}'
    lang_lang = lang_lang.lower()
    lang_info = f'{t_lang[trg_lang-1]}'
    URL = f'https://context.reverso.net/translation/{lang_lang}/{word}'
    try:
        while True:
            r = requests.get(URL, headers={'User-Agent': USER_AGENT})
            if r.status_code == 200:
                # print(str(r.status_code), "OK")
                break
            elif r.status_code == 404:
                print("Sorry, unable to find", word)
                sys.exit()
    except requests.exceptions.ConnectionError:
        print("Something wrong with your internet connection")
        sys.exit()
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup, lang_info

def my_printer(r_soup, l_info, step):
    idx = 0
    my_print(l_info + " Translations:")
    class_list = ["translation ltr dict adv", "translation ltr dict n", "translation ltr dict no-pos"]
    a1 = [t.text.strip() for t in r_soup.find('section', id="top-results").select("a[class^=translation]")]
    for i in a1:
        idx += 1
        my_print(i)
        if idx == step:
            break
    idx = 0
    my_print("\n" + l_info + " Examples:")
    a2 = [e.text.strip() for e in r_soup.find('section', id="examples-content").find_all('span', class_="text")]
    for i in a2:
        idx += 1
        my_print(i)
        if idx == step * 2:
            break
    my_print('\n')


if target_lang != 0:
    sp, langif = my_translator(origin_lang, target_lang)
    my_printer(sp, langif, 10000)
else:
    idx = 0
    for l in t_lang:
        idx += 1
        if l == t_lang[origin_lang-1]:
            continue
        sp, langif = my_translator(origin_lang, idx)
        my_printer(sp, langif, 1)

f.close()
