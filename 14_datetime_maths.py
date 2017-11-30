import datetime as dt
yr, mo, dd = 2012, 12, 21
print(dt.date(yr, mo, dd))
hr, mm, ss, ms= 12, 21, 12, 21
print(dt.time(hr, mm, ss, ms))
d1 = dt.datetime(yr, mo, dd, hr, mm, ss, ms)
d2 = dt.datetime(yr + 1, mo, dd, hr, mm, ss, ms)
print(" d1:" , str(d1),"\n", "d2:", d2)
print("d2 - d1:", d2-d1)
print("d2 + dt.timedelta(30,11,22) -->", d2 + dt.timedelta(30,11,22))
print("dt.date(2012,12,21) + dt.timedelta(30,12,0) -->",dt.date(2012,12,21) + dt.timedelta(30,12,24))
d3 = dt.date(2012,12,21)
print("dt.datetime.combine(d3, dt.time(0))-->", dt.datetime.combine(d3, dt.time(0)))
d4=dt.datetime(2012,12,21,12,21,12,21)
print(d4.replace(month=11,day=10,hour=9,minute=8,second=7,microsecond=6))
