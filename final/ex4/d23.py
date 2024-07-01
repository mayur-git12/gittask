from datetime import date
from dateutil.relativedelta import relativedelta

month = date.today() + relativedelta(months=+1)
print(month)