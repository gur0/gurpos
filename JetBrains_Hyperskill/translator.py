import requests

from bs4 import BeautifulSoup

print('Type "en" if you want to translate from French into English,\
 or "fr" if you want to translate from English into French:')
target_lang = input()
print('Type the word you want to translate:')
word = input()
print(f'You chose "{target_lang}" as the language to translate "{word}".')

lang_lang = ''
if target_lang == "en":
    lang_lang = 'french-english'
elif target_lang == "fr":
    lang_lang = 'english-french'

URL = f'https://context.reverso.net/translation/{lang_lang}/{word}'
USER_AGENT = 'Mozilla/5.0'

while True:
    r = requests.get(URL, headers={'User-Agent': USER_AGENT})
    if r.status_code == 200:
        print(str(r.status_code), "OK")
        break

soup = BeautifulSoup(r.content, 'html.parser')

print("Translations")
class_list = ["translation ltr dict adv", "translation ltr dict n"]
a1 = [t.text.strip() for t in soup.find('section', id="top-results").find_all('a', class_=class_list)]
a2 = [e.text.strip() for e in soup.find('section', id="examples-content").find_all('span', class_="text")]
print(a1)
print(a2)
