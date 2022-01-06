import schedule
from forecast_prophet import forecast

schedule.every().second.do(forecast)
while True:
    schedule.run_pending()
