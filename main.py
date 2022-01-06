import datetime


def test():
    print(cg.get_price(ids='bitcoin', vs_currencies='usd'))
    # print(cg.get_coins_list())

    date_from = datetime.datetime.now() - datetime.timedelta(days=365)
    date_from = str(date_from.utcnow()) + 'Z'

    json_data = cg.get_coin_history_by_id(id='bitcoin', date='01-01-2020')

    market_data = json_data['market_data']
    print(market_data)

    current_price = market_data['current_price']
    print(current_price)

    usd_price = current_price['usd']
    print(usd_price)

    history = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='usd', from_timestamp='1608644629',
                                                   to_timestamp='1640184264')
    print(history)

    for price in history['prices']:
        print(price)


