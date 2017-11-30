#!/usr/bin/python3
import datetime as d
import calendar as c
##
principal=float(input("Enter Principle amount:"))
interest_rate=float(input("Enter annual interest rate:"))
payout_day,payout_month,payout_year=input("..and when do you expect"
                                         +" to get it back: year month day:") \
                                        .split()

now=d.datetime.now()
d0=d.date(now.year, now.month, now.day)
d1=d.date(int(payout_day), int(payout_month), int(payout_year))
interest = principal * interest_rate * (d1-d0).days \
           / ((365 + c.leapdays(d1.year, d0.year))*100)
print("Principal:"+str(principal) + ", Interest:"+str(interest)
     +", Total:"+ str(principal+interest))
