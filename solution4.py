# 1. Write a Python script to display the various Date Time formats - Go to the editor

# a) Current date and time from datetime import datetime

import datetime 
x=datetime.datetime.now()
print(x)

# b) Current year

import datetime
x=datetime.datetime.now()
print(x.strftime("%Y"))


# c) Month of year

import datetime
x=datetime.datetime.now()
print(x.strftime("%m"))

# d) Week number of the year
import datetime
x=datetime.datetime.now()
print(x.strftime("%W"))


# e) Weekday of the week
import datetime
x=datetime.datetime.now()
print(x.strftime("%A"))


# f) Day of year

import datetime
x=datetime.datetime.now()
print(x.strftime("%j"))


# g) Day of the month

import datetime
x=datetime.datetime.now()
print(x.strftime("%d"))

# h) Day of week

import datetime
x=datetime.datetime.now()
print(x.strftime("%w"))