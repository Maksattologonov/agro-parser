import re
import time
import requests
import schedule
import dateutil.parser as dparser

from bs4 import BeautifulSoup
from django.core.management import BaseCommand

from aparser.models import Links, News

URL = 'https://agro.gov.kg/language/ru/category/%d0%bd%d0%be%d0%b2%d0%be%d1%81%d1%82%d0%b8/page/'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/91.0.4472.114 Safari/537.36'
}


def my_parse():
    pages_count = 10

    for page in range(1, pages_count):
        print(f"Парсинг страницы {page}")
        response = requests.get(URL + str(page), headers=HEADERS)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            items = soup.findAll('li', class_='status-publish')
            for item in items:
                detail_parse(item.find('a', class_='post-thumb').get('href'))
        else:
            print("Что-то пошло не так")


def detail_parse(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='main-content')
    components = []
    for item in items:
        title = item.find('h1', class_='post-title').get_text(strip=True)
        image = item.find('img', class_='attachment-full').get('src')
        text = item.find('div', class_='entry-content').get_text(strip=True)
        author = item.find('a', class_='author-name').get_text(strip=True)
        last_updated_date = item.find('span', class_='last-updated').get_text(strip=True)
        last_updated_clear = (dparser.parse(last_updated_date, fuzzy=True).strftime("%Y-%m-%d"))
        print(last_updated_clear)
        if not News.objects.filter(image_id=image).exists():
            query = News.objects.create(title=title, image_id=image, text=text, author=author,
                                        last_updated=last_updated_clear)
            query.save()
            components = [title, image, text, author, last_updated_clear]
            print(components)


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(my_parse())
