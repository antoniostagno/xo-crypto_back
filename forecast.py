from pycoingecko import CoinGeckoAPI
import json
from random import uniform
from datetime import datetime
from models import Forecast


cg = CoinGeckoAPI()


def save_to_db(data):
    # Opening JSON file
    f = open('db.json')

    # returns JSON object as a dictionary
    data_json = json.load(f)

    data_json['data'].append(data)

    with open('db.json', 'w') as outfile:
        json.dump(data_json, outfile)


def forecast():
    now = datetime.utcnow()
    data = cg.get_price(ids='bitcoin', vs_currencies='usd')
    current_price = data['bitcoin']['usd']
    forecast_price = current_price * uniform(0.9,1.1)
    print(data['bitcoin']['usd'], forecast_price)
    Forecast(crypto='bitcoin', current_price=current_price, forecast_price=forecast_price, timestamp=now).insert()
