#Total cases in Australia,India,UK,US till sep 10/21
#Month with highest average number of cases in 2020

#Month with lowest average number of cases in 2021
#Month with highest average number of cases in 2021

import pandas
import csv
from datetime import datetime

monthly_cases = {}
monthly_cases_India = {}
monthly_cases_UK = {}
monthly_cases_US = {}
##month_dict = {
##    'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,
##    'July':7,'August':8,'September':9,'October':10,'November':11,
##    'December':12
##    }
    
is_first_line = True

for row in open("covid_cases.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    date = values[0]
    country = values[2]
    year = date.split('/')[2]
    month = date.split('/')[1]
    if country == 'Australia':
        #date = values[0]
        cases = int(values[4])
        if month in monthly_cases:
            monthly_cases[month].append(cases)
        else:
            monthly_cases[month] = [cases]
            
highest_avg_cases = -1
highest_month = ''
for key in monthly_cases:
    cases = monthly_cases[key]
    avg_cases = sum(cases)/len(cases)
    if avg_cases > highest_avg_cases:
        highest_avg_cases = avg_cases
        highest_month = key
print("{} had the highest average number of cases of {} in Australia.".format(highest_month,highest_avg_cases))
print(monthly_cases)

