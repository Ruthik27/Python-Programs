

name = input("Enter your name : ")
age = int(input("Enter age :"))

from datetime import date
yr = date.today().year

print ("{} will turn 100 year old in the year : {} "
.format(name,yr+100-age))
