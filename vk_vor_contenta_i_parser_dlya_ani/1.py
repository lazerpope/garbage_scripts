tok = ""

TOKEN_USER = tok
# VERSION = #версися api vk
DOMAIN =  'typical_krd'

import requests

# через api vk вызываем статистику постов
response = requests.get('https://api.vk.com/method/wall.get',
params={'access_token': TOKEN_USER,
        'v':'5.199',
        'domain': DOMAIN,
        'count': 30,
                      })

data = response.json()['response']['items']
import json

with open('res.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data))
