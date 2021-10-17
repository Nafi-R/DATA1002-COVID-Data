import pandas as pd
import csv

#Finding the total sum of all cases in each country
df = pd.read_csv('cleaned_datset_cases.csv')
group_by_country = df.groupby('Country')
cases_by_country = group_by_country['New_cases']
total_cases_by_country = cases_by_country.sum()
total = total_cases_by_country.to_dict()
print("\n*** -------------------------------------- ***") 
print('From 3/Jan/20 to 10/Sep/21 total number of cases by country is-\n')
for key, value in total.items():
    print(key, ' : ', value)
print("*** -------------------------------------- ***\n")  

# Creating dictionaries for each month as key and the number of 
# cases per date as values in 2020
is_first_line = True
monthly_cases_aus = {}
monthly_cases_india = {}
monthly_cases_uk = {}
monthly_cases_us= {}

for row in open("cleaned_datset_cases.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    cases = int(values[4])
    date = values[0]
    country = values[2]
    year = date.split('/')[2]
    month = date.split('/')[1]
    if year == '20':
        if country == 'Australia':
            if month in monthly_cases_aus:
                monthly_cases_aus[month].append(cases)
            else:
                monthly_cases_aus[month] = [cases]
        elif country == 'India':
            if month in monthly_cases_india:
                monthly_cases_india[month].append(cases)
            else:
                monthly_cases_india[month] = [cases]
        elif country == 'The United Kingdom':
            if month in monthly_cases_uk:
                monthly_cases_uk[month].append(cases)
            else:
                monthly_cases_uk[month] = [cases]
        elif country == 'United States of America':
            if month in monthly_cases_us:
                monthly_cases_us[month].append(cases)
            else:
                monthly_cases_us[month] = [cases]
#Finding the month with the highest average number of cases for each country
highest_avg_aus = -1
highest_avg_india = -1
highest_avg_uk = -1
highest_avg_us = -1
highest_month_aus = ''
highest_month_india = ''
highest_month_uk = ''
highest_month_us = ''

for key in monthly_cases_aus:
    cases = monthly_cases_aus[key]
    avg_cases = sum(cases)/len(cases)
    if avg_cases > highest_avg_aus:
        highest_avg_aus = avg_cases
        highest_month_aus = key
for key in monthly_cases_india:
    cases = monthly_cases_india[key]
    avg_cases = sum(cases)/len(cases)
    if avg_cases > highest_avg_india:
        highest_avg_india = avg_cases
        highest_month_india = key
for key in monthly_cases_uk:
    cases = monthly_cases_uk[key]
    avg_cases = sum(cases)/len(cases)
    if avg_cases > highest_avg_uk:
        highest_avg_uk = avg_cases
        highest_month_uk = key
for key in monthly_cases_us:
    cases = monthly_cases_us[key]
    avg_cases = sum(cases)/len(cases)
    if avg_cases > highest_avg_us:
        highest_avg_us = avg_cases
        highest_month_us = key
print("\n*** -------------------------------------- ***")  
print("""In 2020 the month with the highest average number of cases are:
      \nAustralia - Month: {}, Highest Average: {:.2f}
      \nIndia - Month: {}, Highest Average: {:.2f}
      \nThe United Kingdom - Month: {}, Highest Average: {:.2f}
      \nUnited States of America - Month: {}, Highest Average: {:.2f}
      """.format(highest_month_aus,highest_avg_aus,highest_month_india,
                 highest_avg_india,highest_month_uk,highest_avg_uk,
                 highest_month_us,highest_avg_us))
print("*** -------------------------------------- ***\n") 
print("") 
is_first_line = True
#Creating dictionary for each countries cases by month in 2021
monthly_cases_aus = {}
monthly_cases_india = {}
monthly_cases_uk = {}
monthly_cases_us= {}

for row in open("cleaned_datset_cases.csv"):
  if is_first_line:
    is_first_line = False
  else:
    values = row.split(",")
    cases = int(values[4])
    date = values[0]
    country = values[2]
    year = date.split('/')[2]
    month = date.split('/')[1]
    if year == '21'and month != 9:
        if country == 'Australia':
            if month in monthly_cases_aus:
                monthly_cases_aus[month].append(cases)
            else:
                monthly_cases_aus[month] = [cases]
        elif country == 'India':
            if month in monthly_cases_india:
                monthly_cases_india[month].append(cases)
            else:
                monthly_cases_india[month] = [cases]
        elif country == 'The United Kingdom':
            if month in monthly_cases_uk:
                monthly_cases_uk[month].append(cases)
            else:
                monthly_cases_uk[month] = [cases]
        elif country == 'United States of America':
            if month in monthly_cases_us:
                monthly_cases_us[month].append(cases)
            else:
                monthly_cases_us[month] = [cases]

#Finding the month with lowest number of cases for each country
lowest_aus = 10000000
lowest_india = 10000000
lowest_uk = 10000000
lowest_us = 10000000
lowest_month_aus = ''
lowest_month_india = ''
lowest_month_uk = ''
lowest_month_us = ''

for key in monthly_cases_aus:
    cases = monthly_cases_aus[key]
    num_cases = sum(cases)
    if num_cases < lowest_aus:
        lowest_aus = num_cases
        lowest_month_aus = key
for key in monthly_cases_india:
    cases = monthly_cases_india[key]
    num_cases = sum(cases)
    if num_cases < lowest_india:
        lowest_india = num_cases
        lowest_month_india = key
for key in monthly_cases_uk:
    cases = monthly_cases_uk[key]
    num_cases = sum(cases)
    if num_cases < lowest_uk:
        lowest_uk = num_cases
        lowest_month_uk = key
for key in monthly_cases_us:
    cases = monthly_cases_us[key]
    num_cases = sum(cases)
    if num_cases < lowest_us:
        lowest_us = num_cases
        lowest_month_us = key
print("\n*** -------------------------------------- ***")     
print("""In 2021 the month with the lowest number of cases are:
      \nAustralia - Month: {}, Number of cases: {}
      \nIndia - Month: {}, Number of cases: {}
      \nThe United Kingdom - Month: {}, Number of cases: {}
      \nUnited States of America - Month: {}, Number of cases: {}
      """.format(lowest_month_aus,lowest_aus,lowest_month_india,
                 lowest_india,lowest_month_uk,lowest_uk,
                 lowest_month_us,lowest_us))
print ("*** -------------------------------------- ***\n")          
            
            

            
            

    
