import time
import datetime
from datetime import date
today = date.today()
print("Today:" + str(today))
datetime.date(2007, 12, 5)
today == date.fromtimestamp(time.time())
my_birthday = date(today.year, 12, 31)
if my_birthday < today:
   my_birthday = my_birthday.replace(year=today.year + 1)
print(str(my_birthday))
datetime.date(2008, 6, 24)
time_to_birthday = abs(my_birthday - today)
print(str(time_to_birthday.days))
