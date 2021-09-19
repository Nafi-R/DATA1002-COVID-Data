import csv

with open("cases.csv","r") as data:
    rdr = csv.reader(data)
    with open("cases_data.csv","w") as output:
        write = csv.writer(output)
        for r in rdr:
            write.writerow((r[0], r[1], r[2], r[3], r[4], r[5]))
            
        with open('cases_data.csv', 'r') as csvfile:
            # handle header line, save it for writing to output file
            header = next(csvfile).strip("\n").split(",")
            reader = csv.reader(csvfile)
            results = filter(lambda row: row[1] == 'AU' or row[1] == 'IN' or row[1] == 'GB' or row[1] == 'US', reader)
            with open('covid_cases.csv', 'w') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(header)
                for result in results:
                    writer.writerow(result)
