import schedule
from forecast import forecast

schedule.every().second.do(forecast)
while True:
    schedule.run_pending()
