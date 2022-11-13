import requests
import os

token = os.getenv('TOKEN')
urls = [
    f'https://www.superheroapi.com/api.php/{token}/search/Hulk',
    f'https://www.superheroapi.com/api.php/{token}/search/Thanos',
    f'https://www.superheroapi.com/api.php/{token}/search/Captain%America',
]

def requests_get(url_all):
    req = (requests.get(url) for url in url_all)
    return req

def parsing():
    superhero = []
    for item in requests_get(urls):
        intelligence = item.json()
        try:
            for power_stats in intelligence['results']:
                superhero.append({
                    'name': power_stats['name'],
                    'intelligence': power_stats['powerstats']['intelligence'],
                })
        except KeyError:
            print(f"Введите другой запрос urls: {urls}")

    intelligence_superhero = 0
    name = ''
    for intelligence_hero in superhero:
        if intelligence_superhero < int(intelligence_hero['intelligence']):
            intelligence_superhero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый умный {name}, IQ: {intelligence_super_hero}")

parsing()