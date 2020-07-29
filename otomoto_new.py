import requests
from lxml import html
import pandas as pd
import json

with open('/Users/floro/Documents/Python/otomoto/volvo.json') as json_file:
    old_offers = json.load(json_file)


def get_offers():
    url = "https://www.otomoto.pl/osobowe/volvo/c30/?search%5Bfilter_enum_fuel_type%5D%5B0%5D=petrol&search" \
          "%5Bfilter_enum_fuel_type%5D%5B1%5D=petrol-lpg&search%5Bfilter_float_engine_power%3Afrom%5D=150&search" \
          "%5Border%5D=created_at%3Adesc&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D= "
    page = requests.get(url)
    tree = html.fromstring(page.content)
    url_list = tree.xpath('//div[@class="offers list"]/article/@data-href')

    with open('/Users/floro/Documents/Python/otomoto/volvo.json', 'w') as json_file:
        json.dump(url_list, json_file)

    # print(*url_list, sep = "\n")

    for i in range(len(url_list)):
        if url_list[i] not in old_offers:
            sendTelegram(url_list[i])


def sendTelegram(message):

    token = '1124378393:AAF6pd24TC11W_SVXBx-J3gY9vcIo358yJ0'
    method = 'sendMessage'
    url = 'https://api.telegram.org/bot{0}/{1}'.format(token, method)

    try:
        response = requests.post(url=url, data={'chat_id': -488297324, 'text': message})
        print(response)
    except Exception as e:
        print(e)

get_offers()

