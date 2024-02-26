import datetime

date1 = datetime.datetime.now()
date2 = date1 - datetime.timedelta(days=1)
diff=abs(date2-date1).total_seconds()
print(diff)
