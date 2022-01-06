from pycoingecko import CoinGeckoAPI


def test4():
    cgg = CoinGeckoAPI()
    print(cgg)
    print('coucou')
    data = cgg.get_price(ids='bitcoin', vs_currencies='usd')
    print(data)


test4()
