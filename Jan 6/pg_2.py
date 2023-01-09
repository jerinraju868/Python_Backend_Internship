''' Write a python program to print current year, month and day	 '''

# importing the date class from datetime module
from datetime import date

# calling the in build funciton to get the year
year = date.today().year

# calling the inbuild funciton date.today().month to get current month
month = date.today().month

# date.today().day is used to get the current day
day = date.today().day

# displaying the year, month, and day
print('Current year  : ', year)
print('Current month : ', month)
print('Current day   : ', day)