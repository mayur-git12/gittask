import datetime
today = datetime.date.today()
someday = datetime.date(2022, 12, 25)
diff = someday - today
print(f'{diff.days} days')