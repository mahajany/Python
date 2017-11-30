import datetime as dt
import time     as T
StartDate=dt.datetime(2008,1,1)
EndDate=dt.datetime(2008,12,31,22,43,56)
Today=dt.date.today()
print (StartDate)
print (EndDate)
StartTime=dt.time(20,34,23)
EndTime=dt.time(21,23,22)

print(StartTime)
print(EndTime)
print (Today)

DateTime = dt.datetime.now()
Today = dt.date.today()
b = Today.isoweekday()
Day = T.strftime("%A")
mm = DateTime.month
yy = DateTime.year
dd = DateTime.day
Date = dt.date(yy,mm,dd)
hh = DateTime.hour
mi = DateTime.minute
TimeStamp = dt.time(hh,mi)
print ("It is now",TimeStamp.strftime("%H:%M:%p"),Day,Date.strftime("%m/%d/%Y"))
