import os
from flask import Flask, request, jsonify
from models import Forecast, app, db
from sqlalchemy import func


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/data", methods=['GET', 'POST'])
def data():
    from_date = request.json['from_date']
    to_date = request.json['to_date']
    forecast = Forecast.query.filter(Forecast.timestamp >= from_date, Forecast.timestamp <= to_date).all()
    print(forecast)
    forecast_data = []
    for fcst in forecast:
        forecast_data.append({'crypto': fcst.crypto,
                              'timestamp': str(fcst.timestamp.isoformat()) + 'Z',
                              'current_price': fcst.current_price,
                              'forecast_price': fcst.forecast_price})

    return jsonify(forecast_data)


@app.route("/list_cryptos", methods=['GET', 'POST'])
def list_cryptos():
    crypto_names = db.session.query(Forecast.crypto).group_by(Forecast.crypto).all()

    print(crypto_names)
    forecast_data = []
    for fcst in crypto_names:
        forecast_data.append({'name': fcst.crypto,
                              'current_price': Forecast.query.filter(Forecast.crypto == fcst.crypto).order_by(
                                  Forecast.id.desc()).first().current_price,
                              'icon': ""})

    return jsonify(forecast_data)


if __name__ == '__main__':
    # if os.environ['ENV'] == 'LOCAL':
    app.run(debug=True)
