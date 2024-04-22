
import requests
from bs4 import BeautifulSoup, Tag, NavigableString
from selenium import webdriver
import typing
def get_text(tag: Tag) -> str:
    _inline_elements = {"a","span","em","strong","u","i","font","mark","label",
    "s","sub","sup","tt","bdo","button","cite","del","b","a","font",}

    def _get_text(tag: Tag) -> typing.Generator:
        for child in tag.children:
            if isinstance(child, Tag):
                # if the tag is a block type tag then yield new lines before after
                is_block_element = child.name not in _inline_elements
                if is_block_element:
                    yield "\n"
                yield from ["\n"] if child.name == "br" else _get_text(child)
                if is_block_element:
                    yield "\n"
            elif isinstance(child, NavigableString):
                yield child.string

    return "".join(_get_text(tag))



fo = open("text.txt", "w", encoding='utf-8')



i = 1
res = []
url = "https://www.webnovelpub.pro/novel/outside-of-time-1480/chapter-908"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("--log-level=3")
prefs = {"profile.managed_default_content_settings.images": 2,
         "profile.default_content_settings.cookies": 2}
options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(options=options)
browser.get(url)

html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')


a = soup.find('section' , 'page-in content-wrap')
# remove adds

for s in soup.select('div.EbcjtZbe'):
    
    s.extract()
for s in soup.select('div#pf-6111-1'):
    s.extract()
book_title = soup.find('a', 'booktitle')
content = soup.find('div', 'chapter-content font_default')

res.append(get_text(content))
next = soup.find('a', 'button nextchap').get('href')

i += 1
while 1:
    print(i)
    url = "https://lightnovelpub.vip" + next
    browser.get(url)

    html = browser.page_source

    soup = BeautifulSoup(html, 'html.parser')
    

    a = soup.find('section' , 'page-in content-wrap')
    # remove adds

    for s in soup.select('div.EbcjtZbe'):
        
        s.extract()
    for s in soup.select('div#pf-6111-1'):
        s.extract()
    book_title = soup.find('a', 'booktitle')
    content = soup.find('div', 'chapter-content font_default')
    res.append(get_text(content))
    i += 1
    try: 
        next = soup.find('a', 'button nextchap').get('href')
    except: 
        break


for line in res:
    try:
        fo.write(line)
        fo.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    except:
        print(line)
        exit()

fo.close()
browser.quit()
