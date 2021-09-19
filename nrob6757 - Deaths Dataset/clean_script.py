import os
import csv
folder = os.path.dirname(os.path.realpath(__file__))

total_deaths_by_country = {} # Key: 'Country', Value: No. of Deaths
new_deaths_by_country = {} # Key: 'Country', Value:{ 'Date' : No of Deaths}
cumulative_death_by_country = {} # Key: 'Country', Value:{ 'Date' : No of Deaths}
headers = []
is_first = True

def reformat_date(input_date) -> str:
    """Reformats the date MM/DD/YY or MM/DD/YYY to DD/MM/YYYY"""
    date_split = input_date.split("/")
    year = date_split[2] if len(date_split[2]) > 2 else "20" + date_split[2]
    return f"{date_split[1]}/{date_split[0]}/{year}"

csv_reader = csv.reader(open(f"{folder}\\time_series_covid19_deaths_global.csv"))
csv_writer = csv.writer(open(f"{folder}\deaths_cleaned.csv", "w", newline=''))
is_first = True
for values in csv_reader:
    if is_first:
            is_first = False
            headers = values
            #Reformat Date Values
            for i in range(4, len(values)):
                headers[i] = reformat_date(headers[i])
            csv_writer.writerow(headers)
    else:
        #If no value is in the first 4 columns, set to 'NaN'
        for i in range(0, 4):
            if values[i] == "":
                values[i] = "NaN"
        #If no value is in the first death column, set to 0
        if values[4] == "":
            values[4] = 0
        #If there is a missing value in a death column, set it to the value before it
        for i in range(5, len(values)):
            if values[i] == "":
                values[i] = int(values[i-1])
    
        csv_writer.writerow(values)
