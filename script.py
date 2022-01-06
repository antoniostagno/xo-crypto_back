from pycoingecko import CoinGeckoAPI
from models import Coin, save_to_db


# insère tous les coins dans la base de données
def import_coins():
    cgg = CoinGeckoAPI()

    data = cgg.get_coins_list()
    for coin in data:
        Coin(symbol=coin.get("symbol"),
             name=coin.get("name"),
             id_gecko=coin.get("id")).quick_save()
    save_to_db()
    print(data)


import_coins()
