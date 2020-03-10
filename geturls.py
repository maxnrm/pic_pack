# -- it would be better to get URLs in the same script as I did everything else
# -- but I can't figure out how to do that fast enough, so though it would be
# -- OK alternative

import json
from requests_html import HTMLSession

# -- load 100 urls from direct request to Yandex.Images
# -- haven't find any clear API or npm module so did it this way

session = HTMLSession()
baseURL = 'https://yandex.ru/images/search?text='

# -- direct request load only about 30 images
# -- (from browser Yandex detect screen size and loads amount of images
# -- depending on it, but haven't find a way to simulate from python script)
# -- so I make a few requests with different search texts
# -- to make sure there will be a 100

texts = ['car', 'cat', 'dog', 'rat', 'tree', 'star']

def get_urls():

    urls = []
    imgs = []

    # -- we get urls of thumbnail images from page Yandex.Images give us with
    # -- request

    for text in texts:
        r = session.get(baseURL + text)
        imgs_chunk = r.html.find('img.serp-item__thumb')
        imgs = imgs + imgs_chunk

    # -- then we append thumb img src attributes to form a list of urls for
    # -- those imgs. this list we'll use in nodejs script to get images

    for img in imgs:
        if len(urls) < 100:
            urls.append('https:' + img.attrs['src'])
        else:
            return urls

    # -- make sure if for some reason there won't be enough imgs
    # -- we still get at least some

    return urls

if __name__ == '__main__':

    urls = get_urls()

    # -- this kinda cheat, but there was no rule to not save URLs to
    # -- filesystem :))

    # -- best way was to make same stuff with nodejs, then I won't need to save
    # -- them to fs but as I said I can't figure out fast enough how to do that
    # -- with node

    with open('urls.json', 'w') as f:
        json.dump(urls, f)

    print('OK')
