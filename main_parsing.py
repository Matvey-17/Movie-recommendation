from bs4 import BeautifulSoup
import requests
import sqlite3

url = 'https://kino.mail.ru/cinema/top/'
url_film = 'https://kino.mail.ru'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
arr_all_name = soup.find_all('span', class_='link__text')
arr_all_genre = soup.find_all('div', class_='p-itemevent-small__info')
arr_all_url = soup.find_all('a',
                            class_='link link_inline link-holder link-holder_itemevent link-holder_itemevent_small')

arr_all_url_film = []
for url in arr_all_url:
    arr_all_url_film.append(url['href'])

arr_all_desc = []
for url_page in arr_all_url_film:
    page_film = requests.get(url_film + url_page)
    soup_film = BeautifulSoup(page_film.text, 'html.parser')
    desc = soup_film.find('div',
                          class_='text text_inline text_light_medium text_fixed valign_baseline p-movie-info__description-text')
    arr_all_desc.append(desc.text)

arr_genre = []
for i in arr_all_genre[::2]:
    if i.find_all('a', class_='p_link_black')[2].text.isdigit():
        arr_genre.append(i.find_all('a', class_='p_link_black')[3].text)
    else:
        arr_genre.append(i.find_all('a', class_='p_link_black')[2].text)

arr_name = []
for name in arr_all_name[0:len(arr_all_name) - 3]:
    arr_name.append(name.text)

film = {}
for name_film, name_genre, desc_film in zip(arr_name, arr_genre, arr_all_desc):
    with sqlite3.connect('Films.db') as db:
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS film(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR,
        genre VARCHAR,
        description TEXT,
        url Text
        )""")
        db.commit()
        cursor.execute(
            f"INSERT INTO film (name, genre, description) VALUES ('{name_film}', '{name_genre}', '{desc_film}')")
        db.commit()
