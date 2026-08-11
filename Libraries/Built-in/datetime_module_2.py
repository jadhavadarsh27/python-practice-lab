from datetime import datetime, date, time, timedelta

today = date.today()
print(today)

current_time = datetime.now()
print(current_time)

future_date = today + timedelta(days = 21)
print(future_date)
