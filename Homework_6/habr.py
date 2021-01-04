import requests
from bs4 import BeautifulSoup

KEYWORDS = ['испания', 'мессенджер', 'web', 'python', 'go', 'it', 'ит', ' id', 'google']


def habr_soup():
    ret = requests.get('https://habr.com/ru/all/')
    soup = BeautifulSoup(ret.text, 'html.parser')
    posts = soup.find_all('article', class_='post')
    return posts


def habr_announce_looker():
    posts = habr_soup()
    articles = []
    for post in posts:
        our_search = post.find_all('div', class_='post__text')
        our_text = list(map(lambda my_text: my_text.text.strip().lower().split(' '), our_search))
        for txt in our_text:
            if any((kw in txt for kw in KEYWORDS)):
                dt = post.find('span', class_='post__time').text
                link = post.find('a', class_='post__title_link')
                url = link.attrs.get('href')
                title = link.text.strip()
                articles.append(f'{dt} - {title} - {url}')
                break
    return articles


def habr_text_looker():
    posts = habr_soup()
    urls = []
    articles_tl = []
    for post in posts:
        link = post.find('a', class_='post__title_link')
        url = link.attrs.get('href')
        urls.append(url)
    for one_url in urls:
        ret_new = requests.get(one_url)
        soup_new = BeautifulSoup(ret_new.text, 'html.parser')
        our_search_new = soup_new.find_all('div', class_='post__text')
        our_text_new = list(map(lambda my_text: my_text.text.strip().lower(), our_search_new))
        for txt_new in our_text_new:
            if any((kw in txt_new for kw in KEYWORDS)):
                dt = soup_new.find('span', class_='post__time').text
                link = soup_new.find('span', class_='post__title-text')
                title = link.text.strip()
                articles_tl.append(f'{dt} - {title} - {one_url}')
                break
    return articles_tl


if __name__ == '__main__':
    result = habr_announce_looker()
    for i in habr_text_looker():
        if i not in result:
            result.append(i)
    for article in result:
        print(article)
