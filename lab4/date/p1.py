import datetime

today = datetime.datetime.now()
five_days = today - datetime.timedelta(days=5)

print(five_days)