import os
import csv

def reformat_date(old_date: str) -> str:
    if "/" in old_date:
        values = old_date.split('/')
        day = int(values[0])
        month = int(values[1])
        year = int(values[2]) if len(values[2]) == 4 else int(values[2]) + 2000
        return f"{day}/{month}/{year}"
    else:
        day = int(old_date[6:])
        month = int(old_date[4:6])
        year = int(old_date[:4])
        return f"{day}/{month}/{year}"



folder = os.path.dirname(os.path.realpath(__file__))
death_reader = csv.reader(open(f"{folder}\\deaths_dataset.csv"))
case_reader = csv.reader(open(f"{folder}\\cases_dataset.csv"))
policy_reader = csv.reader(open(f"{folder}\\policies_dataset.csv"))
integrated_writer = csv.writer(open(f"{folder}\\integrate_dataset.csv","w",newline=''))
# {Key:Country, Value:{Key: Date, Value:{Key: Header, Value :[]}}}
cumulative_death_dict = {}
new_death_dict = {}
new_case_dict = {}
cumulative_case_dict = {}
stringency_dict = {}
government_dict = {}
containment_dict = {}
economic_dict = {}

is_first = True
for row in death_reader:
    if is_first:
        is_first = False
    else:
        country = row[1]
        date = row[0]
        if date == "11/9/2021" or date == "12/9/2021":
            continue
        if country not in cumulative_death_dict:
            cumulative_death_dict[country] = {}
        if date not in cumulative_death_dict[country]:
            cumulative_death_dict[country][date] = int(row[2])
        if country not in new_death_dict:
            new_death_dict[country] = {}
        if date not in new_death_dict[country]:
            new_death_dict[country][date] = int(row[3])
    
is_first = True
for row in case_reader:
    if is_first:
        is_first = False
    else:
        country = row[2]
        if country == "The United Kingdom":
            country = "United Kingdom"
        elif country == "United States of America":
            country = "US"
        date = reformat_date(row[0])
        if country not in cumulative_case_dict:
            cumulative_case_dict[country] = {}
        if date not in cumulative_case_dict[country]:
            cumulative_case_dict[country][date] = int(row[5])
        if country not in new_case_dict:
            new_case_dict[country] = {}
        if date not in new_case_dict[country]:
            new_case_dict[country][date] = int(row[4])


is_first = True
for row in policy_reader:
    if is_first:
        is_first = False
    else:
        country = row[0]
        if country == "United States":
            country = "US"
        
        date = reformat_date(row[1])

        if country not in stringency_dict:
            stringency_dict[country] = {}
        if country not in government_dict:
            government_dict[country] = {}
        if country not in containment_dict:
            containment_dict[country] = {}
        if country not in economic_dict:
            economic_dict[country] = {}
        
        if date not in stringency_dict[country]:
            stringency_dict[country][date] = float(row[2])
        if date not in government_dict[country]:
            government_dict[country][date] = float(row[3])
        if date not in containment_dict[country]:
            containment_dict[country][date] = float(row[4])
        if date not in economic_dict[country]:
            economic_dict[country][date] = float(row[5])

        


        
integrated_writer.writerow(["Date","Country","New Cases","Cumulative Cases", "New Deaths", "Cumulative Deaths", "Stringency Index", "Government Response Index", "Containment Index", "Economic Support Index"])
for country in cumulative_death_dict:
    for date in cumulative_death_dict[country]:
        new_cases = new_case_dict[country][date]
        cum_cases = cumulative_case_dict[country][date]
        cum_death = cumulative_death_dict[country][date]
        new_death = new_death_dict[country][date]
        string_index = stringency_dict[country][date]
        govern_index = government_dict[country][date]
        contain_index = containment_dict[country][date]
        economic_index = economic_dict[country][date]
        row = [date,country,new_cases,cum_cases,new_death,cum_death, string_index, govern_index, contain_index,economic_index]
        integrated_writer.writerow(row)



    