import os
import csv
import datetime
folder = os.path.dirname(os.path.realpath(__file__))

 

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



csv_writer = csv.writer(open(f"{folder}\\deaths_cleaned_filtered_reformated.csv","w", newline=''))
csv_writer.writerow(["Date", "Country", "Cumulative Deaths", "New Deaths"])
for country in cumulative_death_by_country:
    for date in cumulative_death_by_country[country]:
        row = [date,country,cumulative_death_by_country[country][date],new_deaths_by_country[country][date]]
        csv_writer.writerow(row)