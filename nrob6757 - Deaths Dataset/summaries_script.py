import os
import csv
import datetime
folder = os.path.dirname(os.path.realpath(__file__))

def date_to_readable_str(input_date) -> str:
    values = input_date.split("/")
    day = int(values[0])
    month = int(values[1])
    year = int(values[2])
    date_val = datetime.date(year,month,day)
    return date_val.strftime("%d-%b") + "-" +  date_val.strftime("%Y")
    

total_deaths_by_country = {} # Key: 'Country', Value: No. of Deaths
new_deaths_by_country = {} # Key: 'Country', Value:{ 'Date' : No of Deaths}
cumulative_death_by_country = {} # Key: 'Country', Value:{ 'Date' : No of Deaths}
headers = []
is_first = True
csv_reader = csv.reader(open(f"{folder}\\deaths_cleaned.csv"))
for values in csv_reader:
    if is_first:
            is_first = False
            headers = values
    else:
        province = values[0]
        country = values[1]
        if(country != "Australia" and country != "US" and country != "United Kingdom" and country != "India"):
            continue
        if country not in total_deaths_by_country:
            total_deaths_by_country[country] = int(values[-3])
        else:
            total_deaths_by_country[country] += int(values[-3])

        if country not in cumulative_death_by_country:
            cumulative_death_by_country[country] = {}
        #Go from dates 22-Jan-2020 to 10-September-2021
        for date_index in range(4, len(values) - 2):
            if headers[date_index] not in cumulative_death_by_country[country]:
                cumulative_death_by_country[country][headers[date_index]] = int(values[date_index])
            else:
                cumulative_death_by_country[country][headers[date_index]] += int(values[date_index])



for country in cumulative_death_by_country.keys():
    prev_deaths = 0
    for date in cumulative_death_by_country[country].keys():
        new_deaths = cumulative_death_by_country[country][date] - prev_deaths
        new_deaths = new_deaths if new_deaths >= 0 else 0
        prev_deaths = cumulative_death_by_country[country][date]
        if country not in new_deaths_by_country:
            new_deaths_by_country[country] = {}
        new_deaths_by_country[country][date] = int(new_deaths)



print(f"From {date_to_readable_str(headers[4])} to {date_to_readable_str(headers[-3])}")
for country in total_deaths_by_country.keys():
    deaths = "{:,}".format(total_deaths_by_country[country])
    print(f"{country} had {deaths} deaths")
print("")

for country in new_deaths_by_country.keys():
    max_date = ""
    max_death = 0
    for date in new_deaths_by_country[country].keys():
        if new_deaths_by_country[country][date] > max_death:
            max_date = date
            max_death = int(new_deaths_by_country[country][date])
    print(f"The deadliest day in {country} was on {date_to_readable_str(max_date)} with {max_death} deaths")
print("")

print("The average new deaths per day in the month of August 2021: ")
for country in new_deaths_by_country.keys():
    count = 0
    total_new_deaths = 0
    for date in new_deaths_by_country[country].keys():
        values = date.split("/")
        month = int(values[1])
        year = int(values[2])
        if month == 8 and year == 2021:
            count += 1
            total_new_deaths += int(new_deaths_by_country[country][date])
    print(f"{country} had an average of {round(total_new_deaths/count,2)} deaths per day")
print("")