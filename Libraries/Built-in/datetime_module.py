from datetime import datetime, date, time, timedelta

current = datetime.now()
print("Current date and time", current)
#for current date and time

today = date.today()
print("Today's date is: ", today)
#for today's date

date= date(2002,9,27)
print("Create date: ", date)
#for create date

future_date = today + timedelta(days=10)
print("Future date after 10 days: ", future_date)
