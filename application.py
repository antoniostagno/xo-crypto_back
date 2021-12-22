from flask import Flask, request, jsonify
from models import Forecast, app

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/data", methods=['GET', 'POST'])
def data():
    from_date = request.json['from_date']
    to_date = request.json['to_date']
    forecast = Forecast.query.filter(Forecast.timestamp>=from_date, Forecast.timestamp<=to_date).all()
    print(forecast)
    forecast_data = []
    for fcst in forecast:
        forecast_data.append({'crypto': fcst.crypto,
                              'timestamp': str(fcst.timestamp.isoformat())+'Z',
                              'current_price': fcst.current_price,
                              'forecast_price': fcst.forecast_price})

    return jsonify(forecast_data)

